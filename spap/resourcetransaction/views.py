from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json,decimal

# Module Models
from .models import SeedCollection,SeedDistribution,Transaction
from regspecies.models import RegPlantae
from resourcebank.models import SeedDeposit,ResourceDeposit
from speciesdata.models import Plantae

# Collections
class SeedCollectionAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

# Implement Permission and Id validity later On
	def put(self,request):
		collection_data = request.body
		collection_data = json.loads(collection_data)
		regplantae_id = int(collection_data['plant'])
		amount = int(collection_data['coll_amount'])
		# Check for seed collection from registered Species or it is a general transaction
		if 'collfromg' in collection_data:
			try:
				regplantae = RegPlantae.objects.get(regplantae=regplantae_id)
				# Seedcollection 
				seedcollection = SeedCollection()
				seedcollection.collfromg = collection_data['collfromg']
				seedcollection.colltog = collection_data['colltog']
				seedcollection.collfromg_id = int(collection_data['collfromg_id'])
				seedcollection.colltog_id = int(collection_data['colltog_id'])
				seedcollection.collfromU = collection_data['collfromU']
				seedcollection.colltoU = collection_data['colltoU']
				seedcollection.collfromU_id = int(collection_data['collfromU_id'])
				seedcollection.colltoU_id = int(collection_data['colltoU_id'])
				seedcollection.plant = regplantae
				seedcollection.coll_amount = int(collection_data['coll_amount'])
				seedcollection.save()
				# Deduction
				seeddeposit_from = SeedDeposit.objects.get(
					body_id = int(collection_data['collfromg_id']),
					body_type = collection_data['collfromg'],
					source_species = regplantae.plantae
					)
				reduced_balance = seeddeposit_from.balance - amount
				SeedDeposit.objects.filter(
					body_id = int(collection_data['collfromg_id']),
					body_type = collection_data['collfromg'],
					source_species = regplantae.plantae
					).update(balance = reduced_balance)
				resource_from = ResourceDeposit.objects.get(
					body_id = int(collection_data['collfromg_id']),
					body_type = collection_data['collfromg'],
					source_species = int(regplantae.plantae.pk)
					)
				ResourceDeposit.objects.filter(
					body_id = int(collection_data['collfromg_id']),
					body_type = collection_data['collfromg'],
					source_species = int(regplantae.plantae.pk)
					).update(balance = reduced_balance)
				# Addition
				seeddeposit_to = SeedDeposit.objects.get(
					body_id = int(collection_data['colltog_id']),
					body_type = collection_data['colltog'],
					source_species = regplantae.plantae
					)
				added_balance = seeddeposit_to.balance + amount
				SeedDeposit.objects.filter(
					body_id = int(collection_data['colltog_id']),
					body_type = collection_data['colltog'],
					source_species = regplantae.plantae
					).update(balance = added_balance)
				resource_to = ResourceDeposit.objects.get(
					body_id = int(collection_data['colltog_id']),
					body_type = collection_data['colltog'],
					source_species = int(regplantae.plantae.pk)
					)
				ResourceDeposit.objects.filter(
					body_id = int(collection_data['colltog_id']),
					body_type = collection_data['colltog'].
					source_species = int(regplantae.plantae.pk)
					).update(balance = added_balance)
				# Transaction finally done
				tranFrom = ResourceDeposit.objects.get(
					body_id = int(collection_data['collfromg_id']),
					body_type = collection_data['collfromg']
					)
				tranTo = ResourceDeposit.objects.get(
					body_id = int(collection_data['colltog_id']),
					body_type = collection_data['colltog']
					)
				Transaction(
					trantype = 'CO',
					tran_id = int(seedcollection.seedcollection) ,
					trangood = 'SD',
					regbeing_type = 'PL' ,
					regbeing_id = regplantae_id ,
					tranfromg = collection_data['collfromg'] , 
					trantog = collection_data['colltog'] ,
					tranfromg_id = int(collection_data['collfromg_id']) , 
					trantog_id = int(collection_data['colltog_id']) ,
					tranfromU = collection_data['collfromU'] , 
					trantoU = collection_data['colltoU'] , 
					tranfromU_id = int(collection_data['collfromU_id']), 
					trantoU_id = int(collection_data['colltoU_id']) , 
					transaction_amount = int(collection_data['coll_amount']),
					bal_dec_from = tranFrom ,
					bal_add_to = tranTo
					).save()

				data = {'seed_collection':seedcollection.seedcollection}
				return Response(data,status=status.HTTP_200_OK)

			except RegPlantae.DoesNotExist:
				error = {'error' : 'Invalid registered platae ID'}
				return Response(error,status=status.HTTP_400_BAD_REQUEST)
		else:
			try:
				regplantae = RegPlantae.objects.get(regplantae=regplantae_id)
				# Seedcollection 
				seedcollection = SeedCollection()
				seedcollection.colltog_id = int(collection_data['colltog_id'])
				seedcollection.colltoU_id = int(collection_data['colltoU_id'])
				seedcollection.plant = regplantae
				seedcollection.coll_amount = int(collection_data['coll_amount'])
				seedcollection.save()
				Transaction(
					trantype = 'SC',
					tran_id = int(seedcollection.seedcollection) ,
					trangood = 'SD',
					regbeing_type = 'PL' ,
					regbeing_id = regplantae_id ,
					tranfromg = 'BC' , 
					trantog = 'BT' ,
					tranfromg_id = 0 , 
					trantog_id = int(collection_data['colltog_id']) ,
					tranfromU = 'RS' , 
					trantoU = 'BO' , 
					tranfromU_id = 0 , 
					trantoU_id = int(collection_data['colltoU_id']) , 
					transaction_amount = int(collection_data['coll_amount']),
					bal_dec_from = tranFrom ,
					bal_add_to = tranTo
					).save()

				try:
					seeddeposit_to = SeedDeposit.objects.get(
						body_id = int(collection_data['colltog_id']),
						body_type = 'BT',
						source_species = regplantae.plantae
						)
					added_balance = seeddeposit_to.balance + amount
					SeedDeposit.objects.filter(
						body_id = int(collection_data['colltog_id']),
						body_type = 'BT',
						source_species = regplantae.plantae
						).update(balance = added_balance)
					resource_to = ResourceDeposit.objects.get(
						body_id = int(collection_data['colltog_id']),
						body_type = 'BT',
						source_species = int(regplantae.plantae.pk)
						)
					ResourceDeposit.objects.filter(
						body_id = int(collection_data['colltog_id']),
						body_type = 'BT',
						source_species = int(regplantae.plantae.pk)
						).update(balance = added_balance)

					data = {'seed_collection':seedcollection.seedcollection}
					return Response(data,status=status.HTTP_200_OK)

				except SeedDeposit.DoesNotExist:
					# No existing account for the 
					try:
						beat = Beat.objects.get(pk=int(collection_data['colltog_id']))
						seedeposit = SeedDeposit()
						seedeposit.body_type = 'BT'
						seedeposit.body_id = int(collection_data['colltog_id'])
						seedeposit.source_species = regplantae.plantae
						seedeposit.balance = amount
						seedeposit.save()
						resourcedeposit = ResourceDeposit()
						resourcedeposit.body_type = 'BT'
						resourcedeposit.body_id = int(collection_data['colltog_id'])
						resourcedeposit.resource_type = 'SD'
						resourcedeposit.resource_bank_id = seedeposit.account
						resourcedeposit.source_species = int(regplantae.plantae.pk)
						resourcedeposit.balance = amount
						resourcedeposit.save()

						data = {'seed_collection':seedcollection.seedcollection}
						return Response(data,status=status.HTTP_200_OK)

					except Beat.DoesNotExist:
						error = {'error':'Invalid beat ID'}
						return Response(error,status=status.HTTP_400_BAD_REQUEST)

			except RegPlantae.DoesNotExist:
				error = {'error' : 'Invalid registered platae ID'}
				return Response(error,status=status.HTTP_400_BAD_REQUEST)

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(SeedCollectionAPI,self).dispatch(*args, **kwargs)


# Distribution
class SeedDistributionAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	throttle_classes = (UserRateThrottle,)

# Implement Permission and Id validity later On
	def put(self,request):
		distribution_data = request.body
		distribution_data = json.loads(distribution_data)
		regplantae_id = int(distribution_data['plant'])
		amount = int(distribution_data['dis_amount'])
		try:
			regplantae = RegPlantae.objects.get(regplantae=regplantae_id)
			seeddistribution = SeedDistribution()
			seeddistribution.disfromg = distribution_data['disfromg']
			seeddistribution.distog = distribution_data['distog']
			seeddistribution.disfromg_id = int(distribution_data['disfromg_id'])
			seeddistribution.distog_id = int(distribution_data['distog_id'])
			seeddistribution.disfromU = distribution_data['disfromU']
			seeddistribution.distoU = distribution_data['distoU']
			seeddistribution.disfromU_id = int(distribution_data['disfromU_id'])
			seeddistribution.distoU_id = int(distribution_data['distoU_id'])
			seeddistribution.plant = regplantae
			seeddistribution.dis_amount = int(distribution_data['dis_amount'])
			seeddistribution.save()
			# Deduction
			seeddeposit_from = SeedDeposit.objects.get(
				body_id = int(distribution_data['disfromg_id']),
				body_type = distribution_data['disfromg'],
				source_species = regplantae.plantae
				)
			reduced_balance = seeddeposit_from.balance - amount
			SeedDeposit.objects.filter(
				body_id = int(distribution_data['disfromg_id']),
				body_type = distribution_data['disfromg'],
				source_species = regplantae.plantae
				).update(balance = reduced_balance)
			resource_from = ResourceDeposit.objects.get(
				body_id = int(distribution_data['disfromg_id']),
				body_type = distribution_data['disfromg'],
				source_species = int(regplantae.plantae.pk)
				)
			ResourceDeposit.objects.filter(
				body_id = int(distribution_data['disfromg_id']),
				body_type = distribution_data['disfromg'],
				source_species = int(regplantae.plantae.pk)
				).update(balance = reduced_balance)
			# Addition
			seeddeposit_to = SeedDeposit.objects.get(
				body_id = int(distribution_data['distog_id']),
				body_type = distribution_data['distog'],
				source_species = regplantae.plantae
				)
			added_balance = seeddeposit_to.balance + amount
			SeedDeposit.objects.filter(
				body_id = int(distribution_data['distog_id']),
				body_type = distribution_data['distog'],
				source_species = regplantae.plantae
				).update(balance = added_balance)
			resource_to = ResourceDeposit.objects.get(
				body_id = int(distribution_data['distog_id']),
				body_type = distribution_data['distog'],
				source_species = int(regplantae.plantae)
				)
			ResourceDeposit.objects.filter(
				body_id = int(distribution_data['distog_id']),
				body_type = distribution_data['distog'],
				source_species = int(regplantae.plantae)
				).update(balance = added_balance)
			# Transaction finally done
			tranFrom = ResourceDeposit.objects.get(
				body_id = int(distribution_data['disfromg_id']),
				body_type = distribution_data['disfromg']
				)
			tranTo = ResourceDeposit.objects.get(
				body_id = int(distribution_data['distog_id']),
				body_type = distribution_data['distog']
				)
			Transaction(
				trantype = 'DS',
				tran_id = int(seeddistribution.seeddistribution) ,
				trangood = 'SD',
				regbeing_type = 'PL' ,
				regbeing_id = regplantae_id ,
				tranfromg = distribution_data['disfromg'] , 
				trantog = distribution_data['distog'] ,
				tranfromg_id = int(distribution_data['disfromg_id']) , 
				trantog_id = int(distribution_data['distog_id']) ,
				tranfromU = distribution_data['disfromU'] , 
				trantoU = distribution_data['distoU'] , 
				tranfromU_id = int(distribution_data['disfromU_id']) , 
				trantoU_id = int(distribution_data['distoU_id']) , 
				transaction_amount = int(distribution_data['dis_amount']),
				bal_dec_from = tranFrom ,
				bal_add_to = tranTo
				).save()

			data = {'seed_distribution':seeddistribution.seeddistribution}
			return Response(data,status=status.HTTP_200_OK)

		except RegPlantae.DoesNotExist:
			error = {'error':'Invalid RegPlantse ID'}
			return Response(error,status=status.HTTP_400_BAD_REQUEST)


	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(SeedDistributionAPI,self).dispatch(*args, **kwargs)


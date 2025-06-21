from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import PricingConfig, DayBasedPricing
from decimal import Decimal
import math



class CalculatePriceView(View):
    def get(self, request):
        # Get parameters from request
        # Convert all inputs to Decimal for consistency
        distance = Decimal(request.GET.get('distance', 0))
        ride_time = Decimal(request.GET.get('ride_time', 0))
        waiting_time = Decimal(request.GET.get('waiting_time', 0))
        day_of_week = int(request.GET.get('day_of_week', 0))

        try:
            config = PricingConfig.objects.get(is_active=True)
        except PricingConfig.DoesNotExist:
            return JsonResponse({'error': 'No active pricing config'}, status=400)

        try:
            day_pricing = DayBasedPricing.objects.get(config=config, day=day_of_week)
        except DayBasedPricing.DoesNotExist:
            return JsonResponse({'error': 'No pricing for this day'}, status=400)

        # Calculate distance-based price
        if distance <= day_pricing.base_distance:
            distance_price = day_pricing.base_price
        else:
            extra_distance = distance - day_pricing.base_distance
            distance_price = day_pricing.base_price + (extra_distance * day_pricing.additional_price)

        # Calculate time-based price
        time_price = 0
        multipliers = config.time_multipliers.order_by('order')
        remaining_time = ride_time

        for tier in multipliers:
            if remaining_time <= 0:
                break

            time_in_tier = min(remaining_time, tier.duration_upper_bound)
            time_price += time_in_tier * tier.multiplier
            remaining_time -= time_in_tier

        # Calculate waiting charges
        if waiting_time > config.waiting_time_threshold:
            chargeable_time = waiting_time - config.waiting_time_threshold
            waiting_charges = math.ceil(chargeable_time) * config.waiting_charge
        else:
            waiting_charges = 0

        total_price = distance_price + time_price + waiting_charges

        return JsonResponse({
            'price': round(total_price, 2),
            'components': {
                'distance_price': distance_price,
                'time_price': time_price,
                'waiting_charges': waiting_charges
            }
        })

from django.test import TestCase

# Create your tests here.
# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import PricingConfig, DayBasedPricing, TimeMultiplier


class PricingCalculationTests(TestCase):
    def setUp(self):
        self.config = PricingConfig.objects.create(
            name="Test Config",
            is_active=True,
            waiting_charge=5,
            waiting_time_threshold=3
        )

        # Add day pricing
        DayBasedPricing.objects.create(
            config=self.config,
            day=1,  # Monday
            base_distance=3,
            base_price=90,
            additional_price=30
        )

        # Add time multipliers
        TimeMultiplier.objects.bulk_create([
            TimeMultiplier(
                config=self.config,
                duration_upper_bound=60,
                multiplier=1.0,
                order=1
            ),
            TimeMultiplier(
                config=self.config,
                duration_upper_bound=120,
                multiplier=1.25,
                order=2
            ),
            TimeMultiplier(
                config=self.config,
                duration_upper_bound=180,
                multiplier=2.2,
                order=3
            )
        ])

    def test_price_calculation(self):

            url = reverse('calculate-price')
            params = {
                'distance': '5',
                'ride_time': '90',
                'waiting_time': '5',
                'day_of_week': '1'
            }
            response = self.client.get(url, params)
            self.assertEqual(response.status_code, 200)

            data = response.json()

            # Option 1: Exact string comparison
            self.assertEqual(data['price'], '257.50')

            # Option 2: Numeric comparison (more flexible)
            self.assertAlmostEqual(float(data['price']), 257.5, places=2)

            # Verify all components
            self.assertEqual(float(data['components']['distance_price']), 150)
            self.assertEqual(float(data['components']['time_price']), 97.5)
            self.assertEqual(float(data['components']['waiting_charges']), 10)

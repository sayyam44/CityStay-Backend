from django.test import TestCase
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class ListingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_create_listing(self):
        listing = Listing.objects.create(
            seller=self.user,
            title="Test Listing",
            description="Test description",
            area="Inner St.John's",
            listing_type="Apartment",
            property_status="Rent",
            price=1200,
            rental_frequency="Month",
            rooms=2,
            furnished=True,
            utilities=True,
            petfriendly=False,
            cctv=False,
            parking=True,
            address="123 Test St",
            latitude=47.5615,
            longitude=-52.7126
        )
        self.assertEqual(str(listing), "Test Listing")

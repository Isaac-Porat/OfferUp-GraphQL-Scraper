from object import OfferUpScraper

scraper = OfferUpScraper(shoe_type="air force 1", distance=10, delivery_method="p", zipcode="90210", price_percentage_evaluation=0.2, reference_price=100)
scraper.run()

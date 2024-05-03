import requests
import uuid
import pandas as pd
import time

scraping_url = 'https://offerup.com/api/graphql'

with open('locations.txt', 'r') as f, open('sneakers.txt', 'r') as sneakers_file:
    sneakers = [sneaker.strip() for sneaker in sneakers_file.readlines()]

    start_time = time.time()

    for line in f.readlines():
        locations = line.strip().split(',')
        if len(locations) >= 3:
            city = locations[0]
            state = locations[1]
            zip_code = locations[2]

            for sneaker in sneakers:
                delivery_flag = 'p_s' # local = p, shipping = s, local + shipping = p_s
                distance = 50 # 5, 10, 15, 20, 25, 30, 50
                query_value = sneaker
                zip_code = zip_code

                results_df = pd.DataFrame(columns=['Title', 'Price', 'Location', 'URL', 'Image URL'])

                search_session_id = str(uuid.uuid4())
                print(f"UUID: {search_session_id}")

                payload = {"operationName":"GetModularFeed","variables":{"debug":False,"searchParams":[{"key":"DELIVERY_FLAGS","value":f"{delivery_flag}"},{"key":"DISTANCE","value":f"{distance}"},{"key":"q","value":f"{query_value}"},{"key":"platform","value":"web"},{"key":"zipcode","value":f"{zip_code}"},{"key":"experiment_id","value":"experimentmodel24"},{"key":"limit","value":"50"},{"key":"searchSessionId","value":search_session_id}]},
                "query":"query GetModularFeed($searchParams: [SearchParam], $debug: Boolean = false) {\n  modularFeed(params: $searchParams, debug: $debug) {\n    analyticsData {\n      requestId\n      searchPerformedEventUniqueId\n      searchSessionId\n      __typename\n    }\n    categoryInfo {\n      categoryId\n      isForcedCategory\n      __typename\n    }\n    feedAdditions\n    filters {\n      ...modularFilterNumericRange\n      ...modularFilterSelectionList\n      __typename\n    }\n    legacyFeedOptions {\n      ...legacyFeedOptionListSelection\n      ...legacyFeedOptionNumericRange\n      __typename\n    }\n    looseTiles {\n      ...modularTileBanner\n      ...modularTileBingAd\n      ...modularTileGoogleDisplayAd\n      ...modularTileJob\n      ...modularTileEmptyState\n      ...modularTileListing\n      ...modularTileLocalDisplayAd\n      ...modularTileSearchAlert\n      ...modularTileSellerAd\n      ...modularModuleTileAdsPostXAd\n      __typename\n    }\n    modules {\n      ...modularGridModule\n      __typename\n    }\n    pageCursor\n    query {\n      ...modularQueryInfo\n      __typename\n    }\n    requestTimeMetadata {\n      resolverComputationTimeSeconds\n      serviceRequestTimeSeconds\n      totalResolverTimeSeconds\n      __typename\n    }\n    searchAlert {\n      alertId\n      alertStatus\n      __typename\n    }\n    debugInformation @include(if: $debug) {\n      rankedListings {\n        listingId\n        attributes {\n          key\n          value\n          __typename\n        }\n        __typename\n      }\n      lastViewedItems {\n        listingId\n        attributes {\n          key\n          value\n          __typename\n        }\n        __typename\n      }\n      categoryAffinities {\n        affinity\n        count\n        decay\n        affinityOwner\n        __typename\n      }\n      rankingStats {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment modularFilterNumericRange on ModularFeedNumericRangeFilter {\n  isExpandedHighlight\n  lowerBound {\n    ...modularFilterNumericRangeBound\n    __typename\n  }\n  shortcutLabel\n  shortcutRank\n  subTitle\n  targetName\n  title\n  type\n  upperBound {\n    ...modularFilterNumericRangeBound\n    __typename\n  }\n  __typename\n}\n\nfragment modularFilterNumericRangeBound on ModularFeedNumericRangeFilterNumericRangeBound {\n  label\n  limit\n  placeholderText\n  targetName\n  value\n  __typename\n}\n\nfragment modularFilterSelectionList on ModularFeedSelectionListFilter {\n  targetName\n  title\n  subTitle\n  shortcutLabel\n  shortcutRank\n  type\n  isExpandedHighlight\n  options {\n    ...modularFilterSelectionListOption\n    __typename\n  }\n  __typename\n}\n\nfragment modularFilterSelectionListOption on ModularFeedSelectionListFilterOption {\n  isDefault\n  isSelected\n  label\n  subLabel\n  value\n  __typename\n}\n\nfragment legacyFeedOptionListSelection on FeedOptionListSelection {\n  label\n  labelShort\n  name\n  options {\n    default\n    label\n    labelShort\n    selected\n    subLabel\n    value\n    __typename\n  }\n  position\n  queryParam\n  type\n  __typename\n}\n\nfragment legacyFeedOptionNumericRange on FeedOptionNumericRange {\n  label\n  labelShort\n  leftQueryParam\n  lowerBound\n  name\n  options {\n    currentValue\n    label\n    textHint\n    __typename\n  }\n  position\n  rightQueryParam\n  type\n  units\n  upperBound\n  __typename\n}\n\nfragment modularTileBanner on ModularFeedTileBanner {\n  tileId\n  tileType\n  title\n  __typename\n}\n\nfragment modularTileBingAd on ModularFeedTileBingAd {\n  tileId\n  bingAd {\n    ouAdId\n    adExperimentId\n    adNetwork\n    adRequestId\n    adTileType\n    adSettings {\n      repeatClickRefractoryPeriodMillis\n      __typename\n    }\n    bingClientId\n    clickFeedbackUrl\n    clickReturnUrl\n    contentUrl\n    deepLinkEnabled\n    experimentDataHash\n    image {\n      height\n      url\n      width\n      __typename\n    }\n    impressionFeedbackUrl\n    impressionUrls\n    viewableImpressionUrls\n    installmentInfo {\n      amount\n      description\n      downPayment\n      __typename\n    }\n    itemName\n    lowPrice\n    price\n    searchId\n    sellerName\n    templateFields {\n      key\n      value\n      __typename\n    }\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularTileGoogleDisplayAd on ModularFeedTileGoogleDisplayAd {\n  tileId\n  googleDisplayAd {\n    ouAdId\n    additionalSizes\n    adExperimentId\n    adHeight\n    adNetwork\n    adPage\n    adRequestId\n    adTileType\n    adWidth\n    adaptive\n    channel\n    clickFeedbackUrl\n    clientId\n    contentUrl\n    customTargeting {\n      key\n      values\n      __typename\n    }\n    displayAdType\n    errorDrawable {\n      actionPath\n      listImage {\n        height\n        url\n        width\n        __typename\n      }\n      __typename\n    }\n    experimentDataHash\n    formatIds\n    impressionFeedbackUrl\n    personalizationProperties {\n      key\n      values\n      __typename\n    }\n    prebidConfigs {\n      key\n      values {\n        timeout\n        tamSlotUUID\n        liftoffPlacementIDs\n        __typename\n      }\n      __typename\n    }\n    renderLocation\n    searchId\n    searchQuery\n    templateId\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularTileJob on ModularFeedTileJob {\n  tileId\n  tileType\n  job {\n    address {\n      city\n      state\n      zipcode\n      __typename\n    }\n    companyName\n    datePosted\n    image {\n      height\n    url\n    width\n    __typename\n  }\n    industry\n    jobId\n    jobListingUrl\n    jobOwnerId\n    pills {\n      text\n      type\n      __typename\n    }\n    title\n    apply {\n      method\n      value\n      __typename\n    }\n    wageDisplayValue\n    provider\n    __typename\n  }\n  __typename\n}\n\nfragment modularTileEmptyState on ModularFeedTileEmptyState {\n  tileId\n  tileType\n  title\n  description\n  iconType\n  __typename\n}\n\nfragment modularTileListing on ModularFeedTileListing {\n  tileId\n  listing {\n    ...modularListing\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularListing on ModularFeedListing {\n  listingId\n  conditionText\n  flags\n  image {\n    height\n    url\n    width\n    __typename\n  }\n  isFirmPrice\n  locationName\n  price\n  title\n  vehicleMiles\n  __typename\n}\n\nfragment modularTileLocalDisplayAd on ModularFeedTileLocalDisplayAd {\n  tileId\n  localDisplayAd {\n    ouAdId\n    adExperimentId\n    adNetwork\n    adRequestId\n    adTileType\n    advertiserId\n    businessName\n    callToAction\n    callToActionType\n    clickFeedbackUrl\n    contentUrl\n    experimentDataHash\n    headline\n    image {\n      height\n      url\n      width\n      __typename\n    }\n    impressionFeedbackUrl\n    searchId\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularTileSearchAlert on ModularFeedTileSearchAlert {\n  tileId\n  tileType\n  title\n  __typename\n}\n\nfragment modularTileSellerAd on ModularFeedTileSellerAd {\n  tileId\n  listing {\n    ...modularListing\n    __typename\n  }\n  sellerAd {\n    ouAdId\n    adId\n    adExperimentId\n    adNetwork\n    adRequestId\n    adTileType\n    clickFeedbackUrl\n    experimentDataHash\n    impressionFeedbackUrl\n    searchId\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularModuleTileAdsPostXAd on ModularFeedTileAdsPostXAd {\n  ...modularTileAdsPostXAd\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularTileAdsPostXAd on ModularFeedTileAdsPostXAd {\n  tileId\n  adsPostXAd {\n    ouAdId\n    adExperimentId\n    adNetwork\n    adRequestId\n    adTileType\n    clickFeedbackUrl\n    experimentDataHash\n    impressionFeedbackUrl\n    searchId\n    offer {\n      beacons {\n        noThanksClick\n        close\n        __typename\n      }\n      title\n      description\n      clickUrl\n      image\n      pixel\n      ctaYes\n      ctaNo\n      __typename\n    }\n    __typename\n  }\n  tileType\n  __typename\n}\n\nfragment modularGridModule on ModularFeedModuleGrid {\n  moduleId\n  collection\n  formFactor\n  grid {\n    actionPath\n    tiles {\n      ...modularModuleTileBingAd\n      ...modularModuleTileGoogleDisplayAd\n      ...modularModuleTileListing\n      ...modularModuleTileLocalDisplayAd\n      ...modularModuleTileSellerAd\n      __typename\n    }\n    __typename\n  }\n  moduleType\n  rank\n  rowIndex\n  searchId\n  subTitle\n  title\n  infoActionPath\n  feedIndex\n  __typename\n}\n\nfragment modularModuleTileBingAd on ModularFeedTileBingAd {\n  ...modularTileBingAd\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularModuleTileGoogleDisplayAd on ModularFeedTileGoogleDisplayAd {\n  ...modularTileGoogleDisplayAd\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularModuleTileListing on ModularFeedTileListing {\n  ...modularTileListing\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularModuleTileLocalDisplayAd on ModularFeedTileLocalDisplayAd {\n  ...modularTileLocalDisplayAd\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularModuleTileSellerAd on ModularFeedTileSellerAd {\n  ...modularTileSellerAd\n  moduleId\n  moduleRank\n  moduleType\n  __typename\n}\n\nfragment modularQueryInfo on ModularFeedQueryInfo {\n  appliedQuery\n  decisionType\n  originalQuery\n  suggestedQuery\n  __typename\n}\n"}

                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Cookie': 'DX=web-8a3ff805a708131d76d62a800c628c1eae0d3e724ac64018a33fc705; ou.ftue=1; ou.color-mode=light; OU.USER_CONTEXT_COOKIE={%22device_id%22:%22web-8a3ff805a708131d76d62a800c628c1eae0d3e724ac64018a33fc705%22%2C%22user_agent%22:%22Mozilla/5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit/537.36%20(KHTML%2C%20like%20Gecko)%20Chrome/124.0.0.0%20Safari/537.36%22%2C%22device_platform%22:%22web%22}; ou.location.jobs={%22city%22:%22Clayton%22%2C%22state%22:%22CA%22%2C%22zipCode%22:%2294517%22%2C%22longitude%22:-121.9146%2C%22latitude%22:37.915%2C%22source%22:%22ip%22}; _lr_geo_location_state=CA; _lr_geo_location=US; cf_clearance=BjmUwaCmKOBBr7VcOmwnqe.ufwclAQMjJOF84_eKfVI-1714423642-1.0.1.1-N9584TyXkS052._e7V3nBwpEZNEXPfgAkjZKbtvN9VGy6iSn8wA5NrInq6OSWa.1ESB16OBm2wABh31k_twVng; ou.session-id=web-8a3ff805a708131d76d62a800c628c1eae0d3e724ac64018a33fc705@1714430470176; ou.location={%22city%22:%22Boston%22%2C%22state%22:%22MA%22%2C%22zipCode%22:%2202108%22%2C%22longitude%22:-71.0661193%2C%22latitude%22:42.3548561%2C%22source%22:%22zipcode%22}; __cf_bm=Il77MDpBKP87BESsHTprCZFIbdsTJE5c1ALLNUZvjAo-1714430470-1.0.1.1-NQ3Dm8MlHNNeOCG2IqrYGNmVrGkYQaFpnsBCGacEatevv.cII4wR1zyHvTyUHZj7zzOTQG557s_zWB1u1UkMDA; _dd_s=rum=0&expire=1714431955300; ou.session-time=1714431055494',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'X-User-Context': '{"device_id":"web-8a3ff805a708131d76d62a800c628c1eae0d3e724ac64018a33fc705","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","device_platform":"web"}',
                    'Origin': 'https://offerup.com',
                    'Referer': 'https://offerup.com/search?q=jordan+4'
                }

                response = requests.post(scraping_url, headers=headers, json=payload)

                print(response.status_code)
                print(response)

                if response.status_code == 200:
                    data = response.json()
                else:
                    print("Failed to fetch data:", response.status_code)

                data = data['data']['modularFeed']['looseTiles']

                for i in data:
                    if 'listing' in i:
                        url = i["listing"]["listingId"]
                        imageUrl = i['listing']['image']['url']
                        location = i['listing']['locationName']
                        price = i['listing']['price']
                        title = i['listing']['title']

                        new_row = {
                            'Title': title,
                            'Price': price,
                            'Location': location,
                            'URL': url,
                            'Image URL': imageUrl
                        }

                        print(new_row)

                state_file = f'output/{state}.csv'
                results_df.to_csv(state_file, mode='w', header=True, index=False)

                print('.', flush=True)



    end_time = time.time()
    print(f"Scraping ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")

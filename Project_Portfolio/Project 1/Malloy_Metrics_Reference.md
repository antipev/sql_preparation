# Retail Media Metrics: Malloy Project Reference

Metrics defined in the cae_retail_media Malloy project. Each row gives the metric, a short definition, and the Malloy measure it comes from.

## 1. Delivery

| Metric | Definition | Malloy measure |
|---|---|---|
| Impressions | Number of times an ad was shown. | Sum_impressions (hourly) |
| Clicks | Number of ad clicks, before deduplication. | Sum_clicks (hourly) |
| Charged clicks | Clicks left after removing duplicate or fraudulent clicks. Billing is based on these. | Sum_charged_clicks (hourly) |
| Charged impressions | Impressions that were billed. | Sum_charged_impressions (hourly) |
| Click-through rate (CTR) | Charged clicks divided by impressions. Blank when there are no impressions. | Click_through_rate_CTR (hourly) |

## 2. Spend

| Metric | Definition | Malloy measure |
|---|---|---|
| Ad spend on clicks | Amount spent on clicks, in minor currency units (cents). | Sum_ad_spent_clicks (hourly) |
| Ad spend on impressions | Amount spent on impressions, in minor currency units. | Sum_ad_spent_impressions (hourly) |
| Ad spend on attributed purchases | Amount spent on purchases the ad is credited for, in minor currency units. | Sum_ad_spent_attributed_purchases (hourly) |
| Pinned campaign spend | Amount spent on exclusive or pinned campaigns, in minor currency units. | Sum_pinned_campaign_spent (hourly) |
| Cost per click (CPC) | Click spend divided by charged clicks, converted to major currency units (divided by 100). | Cost_per_click_ratio_CPC (hourly) |

## 3. Purchases and returns

| Metric | Definition | Malloy measure |
|---|---|---|
| Purchases | Number of purchases attributed to the campaign. | Sum_total_purchase_count (hourly) |
| Purchase quantity | Total number of items in attributed purchases. | Sum_total_purchase_quantity (hourly) |
| Purchase amount | Sales value of attributed purchases (quantity times item price), in minor currency units. | Sum_total_purchase_amount (hourly) |
| Charged attributed purchases | Attributed purchases that were billed. | Sum_charged_attributed_purchases (hourly) |
| Conversion rate (CVR) | Purchases divided by charged clicks. Blank when there are no charged clicks. | Conversion_rate_CVR (hourly) |
| Return on ad spend (ROAS) | Purchase amount divided by click spend. Both are in minor units, so the result is a plain ratio. | Return_on_ad_spend_ratio_ROAS (hourly) |

## 4. Customer segments

| Metric | Definition | Malloy measure |
|---|---|---|
| New customers | Users with no prior order history at the vendor. Counted as distinct users. | Sum_new_user_count (hourly); Distinctcount_new_users (attributions) |
| Returning customers | Users who ordered within 90 days before the purchase at this vendor. | Sum_returning_user_count (hourly); Distinctcount_returning_users (attributions) |
| Winback customers | Users with prior orders at the vendor, but none within the last 90 days. | Sum_winback_user_count (hourly); Distinctcount_winback_users (attributions) |
| Skip Plus customers | Users with an active Skip Plus membership at the time of purchase. | Sum_skip_plus_user_count (hourly); Distinctcount_skip_plus_users (attributions) |
| Segment purchases and amounts | Purchase counts, item quantities and purchase amounts split the same way by segment (new, returning, winback, Skip Plus). | Sum_<segment>_purchase_count, _purchase_quantity, _purchase_amount (hourly) |

## 5. Budget

| Metric | Definition | Malloy measure |
|---|---|---|
| Budget limit | Maximum budget cap for a sponsored ad period, in minor units. | Sum_budget_limit (sponsored_ad_budget) |
| Used budget | Budget consumed so far in the period, in minor units. | Sum_used_budget (sponsored_ad_budget) |
| Budget clicks | Clicks recorded against the sponsored ad budget. | Sum_clicks (sponsored_ad_budget) |

## 6. Campaign setup (dimensions and counts)

| Metric | Definition | Malloy measure |
|---|---|---|
| Campaign count | Number of campaign records. | Count (campaigns) |
| Budget | Campaign budget in cents. Total for corporate campaigns; weekly budget for sponsored ads. | Budget (campaigns) |
| Target ROAS | Target return on ad spend set for the campaign. | Target_roas (campaigns) |
| Bidding type | Bidding model used, such as CPC, CUSTOM or AUTO_BIDDING. | Bidding_type (campaigns) |

## Watch-outs

- Money is stored in minor units (cents). Only CPC divides by 100. ROAS does not need it, since both sides are in cents.
- Daily, weekly and monthly views take customer counts from the attribution table as distinct counts. Summing the hourly user counts would count the same user once per hour.

- CTR and CPC use charged clicks, not raw clicks. Raw clicks are shown for reference only.
- The attribution table does not yet have marketplace_name (pending dbt refresh), so marketplace filters rely on the hourly table.

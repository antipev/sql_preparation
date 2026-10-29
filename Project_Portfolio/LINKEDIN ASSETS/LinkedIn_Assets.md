# LinkedIn Assets — Useful Links



| # | Asset | Theme | Type | Link |
|---|---|---|---|---|
| 1 | Modeling Techniques 1 | Data modeling | LinkedIn post | [lnkd.in/p/gwGCFsuf](https://lnkd.in/p/gwGCFsuf) |
| 2 | Modeling Techniques 2 | Data modeling | LinkedIn post | [lnkd.in/p/gBDYY9gm](https://lnkd.in/p/gBDYY9gm) |
| 3 | Modeling Techniques 3 | Data modeling | LinkedIn post | [lnkd.in/p/gQQqtuwc](https://lnkd.in/p/gQQqtuwc) |
| 4 | Leadership | Leadership and mentoring | LinkedIn post | [lnkd.in/p/gEG2m7Sg](https://lnkd.in/p/gEG2m7Sg) |
| 5 | Malloy Publisher | BI, semantic layer and MCP | Live app | [malloy-publisher-mcp-bolcwt6srq-nn.a.run.app](https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app/) |

---



## Connect your Agent to MCP

**Endpoint (Streamable HTTP, no auth):** `https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app/mcp`

Paste this into your MCP client config, then restart the client:

```json
{
  "mcpServers": {
    "malloy-publisher": {
      "type": "http",
      "url": "https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app/mcp"
    }
  }
}
```

Any client with Streamable HTTP support (Claude, Cursor, Cline, VS Code) uses the same URL. Claude Desktop needs the `mcp-remote` bridge. Once connected, ask: *"List the environments, then show revenue by month."*

**Test without a client:**

```bash
curl -s https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}'
```

- The `Accept` header must include `text/event-stream`, otherwise the server rejects the call.
- Start with `malloy_getContext` (no arguments) to list environments, packages and sources.
- Tools: `malloy_getContext`, `malloy_executeQuery`, `malloy_compile`, `malloy_reloadPackage`, `malloy_searchDatabaseSchema`, `malloy_searchDocs`.
- The BI UI is the same host: https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app/
- Checked 2026-10-28: `/mcp` initialize returned `malloy-publisher-mcp-server` v0.0.1 (protocol `2024-11-05`); `/` and `/health` returned 200.

---

## Example: one general prompt, end to end

Recorded 2026-10-28. Client: **Cline**, model: **DeepSeek**. The prompt is deliberately general, so it can be reused on any package.

**Prompt (sent as-is):**

```text
Analyse the data in the jaffle_shop package on my Malloy Publisher MCP server.
Start with malloy_getContext. Tell me which sources exist, what each one carries,
how many rows each has, the three business questions I can answer today, and the
one thing I cannot. Show the query you ran.
```

**Calls the model made, in order:** `malloy_getContext` (`environmentName`, `packageName`, `query`) -> `malloy_executeQuery` (one per-stage rollup that answers all three questions) -> `malloy_executeQuery` (product-level margin).

**Response:**

```text
The jaffle_shop package lives in environment `workspace`, which also holds
thelook_ecommerce and comics. It publishes exactly one source.

cafe_bridge_explore  (3_explores/cafe_bridge_explore.malloy)
A Unified Star Schema bridge: one row per record per reporting table, every key
column side by side, plus a Stage column naming the table the row came from.
Joined entities: cafe_customers, cafe_locations, cafe_order_items.
Measures it exposes: Total_Revenue, Gross_Margin, Total_Subtotal, Item_Revenue,
Item_Gross_Margin, Order_Count, Order_Item_Count, Customer_Count,
Returning_Customer_Count, Returning_Customer_Rate, Average_Lifetime_Orders,
Average_Lifetime_Spend, Average_Order_Value, Average_Product_Price,
Product_Count, Location_Count, Bridge_Row_Count.
Dimensions: Stage, the six _Key_* columns, Customer_id, Customer_name,
Order_date, First_order_date, Last_order_date, Product_name, Location_name.

Rows per stage:
  cafe_order_items  997      cafe_orders   686     cafe_customers  128
  cafe_supplies      65      cafe_products  10     cafe_locations    6

Query run (one query, because every measure is already stage-scoped):
  run: cafe_bridge_explore -> {
    group_by: Stage
    aggregate:
      Bridge_Row_Count
      cafe_orders.Order_Count
      cafe_orders.Total_Revenue
      cafe_orders.Gross_Margin
      cafe_orders.Average_Order_Value
      cafe_customers.Customer_Count
      cafe_customers.Returning_Customer_Count
      cafe_customers.Returning_Customer_Rate
      cafe_customers.Average_Lifetime_Orders
      cafe_customers.Average_Lifetime_Spend
      cafe_order_items.Order_Item_Count
      cafe_order_items.Item_Revenue
      cafe_order_items.Item_Gross_Margin
      cafe_locations.Location_Count
    order_by: Stage
  }

Three questions you can answer today:
1. Which products earn the margin? "for richer or pourover" $1,176 revenue on
   $1,038.24 margin, "vanilla ice" $960 / $713.60, "tangaroo" $924 / $797.72,
   "chai and mighty" $790 / $513.50, "adele-ade" $660 / $556.05. Those five
   carry 66.1% of item revenue. Thinnest margin: "doctor stew", $407 revenue on
   $314.13 margin.
2. Who buys, and do they come back? 128 customers, 118 of them returning
   (92.2%), 5.36 orders and $56.46 lifetime spend per customer on average.
3. How is the business doing? 686 orders, $7,226.67 revenue, $5,820.95 gross
   margin (80.5%), average order value $10.53. Order items: 997 lines, $6,818
   item revenue and $5,412.28 item margin (79.4%) - the $408.67 difference is tax.

The one thing you cannot answer: which store performs best. Six locations are
modelled - Philadelphia, San Francisco, Brooklyn, Los Angeles, Chicago, New
Orleans - but all 686 orders sit in Philadelphia and the other five report 0.
The same limit blocks any trend question: the history is 16 days, 1-16
September 2016.

Caveat: keys are NULL outside their own stage, so constrain one Stage per query
(or use the pick pattern), otherwise row counts multiply.
```

**What this example shows:**

- The model grounded every name in what the server returned instead of guessing table or field names.
- It answered money and retention questions from the published measures and cross-checked itself in public: 92.2% returning = 118/128, and $56.46 lifetime spend = $7,226.67/128.
- It named the real limits - one store out of six, sixteen days of history - rather than padding the answer.
- Every figure above is reproducible: same prompt, same package, any MCP client.

Note: on a cold replica the server can answer a valid `malloy_executeQuery` with a misleading `Resource not found: ...cafe_bridge_explore.malloy`; repeating the identical call succeeds.


## Using Credible Platform (Only Private access)
https://maxantipev.admin.credibledata.com/


Only one queryable source is exposed. I'll pull its full field list and docs.

The data covers only 16 days (1–16 September 2016). Next I'm checking whether orders can be broken down by location name, since every bridge row carries just one table's key.

Orders join through to location names, so revenue by store works. I'm running the three candidate business questions to confirm each one returns data.

The jaffle_shop package (version 0.1.7) gives you one queryable source, `cafe_bridge_explore`, which joins six café reporting tables. Together they hold 16 days of trading, 1–16 September 2016, from a single store. You can answer questions about product margin, customer retention and order economics. You can't compare stores.

(The tool I ran is called `get_context` here; it does the same job as `malloy_getContext`.)

### Sources and row counts

`cafe_bridge_explore` is a Unified Star Schema explore. Each bridge row belongs to one table (`Stage`) and only that table's key is filled in, so the model's own docs say to filter to one `Stage` per query. The other six tables are joins reached through it:

| Stage | Bridge_Row_Count | What it carries |
|---|---|---|
| cafe_customers | 128 | Name, lifetime orders, first and last order date, lifetime spend (with and without tax), new or returning type |
| cafe_locations | 6 | Store name, tax rate, opening date |
| cafe_orders | 686 | Subtotal, tax, total, order date, order cost, item counts, food and drink flags, and a join to location |
| cafe_order_items | 997 | Product name and price at time of order, supply cost, food and drink flags, and a join to product |
| cafe_products | 10 | Product type, description, menu price, food and drink flags |
| cafe_supplies | 65 | Supply name, cost, perishable flag |

The package has no pre-built views. As a cross-check, customer lifetime spend adds up to the same total as order revenue ($7,226.67), so the customer and order tables agree.

### Query I ran for row counts

```malloy
run: cafe_bridge_explore -> {
  group_by: Stage
  aggregate: Bridge_Row_Count
  order_by: Stage
}
```

### Three questions you can answer today

1. **Which products make the most margin?** The query groups `cafe_order_items.Product_name` with `Item_Revenue` and `Item_Gross_Margin`, filtered to `Stage = 'cafe_order_items'`. "for richer or pourover" leads: 168 units, $1,176 of revenue and $1,038.24 of margin. "doctor stew" is last of the 10 products at $314.13. Across all items, revenue is $6,818 before tax against $1,405.72 of supply cost.
2. **How loyal are customers?** Of 128 customers, 118 have ordered more than once, a returning rate of 92.2%. On average each has placed about 5.4 orders and spent $56.46.
3. **What does a typical order look like?** There are 686 orders bringing in $7,226.67 of revenue including tax. The average order is $10.53 and gross margin is $5,820.95. The food and drink flags let you split these figures further.

### The one thing you can't answer

**How stores compare.** The model lists 6 locations, but when orders are grouped by `cafe_orders.cafe_locations.Location_name`, every one of the 686 orders belongs to Philadelphia. The join works; the other five stores just have no orders in the data.

Separately, with only 16 days of data, any trend is limited to day-by-day or week-by-week patterns within that window.
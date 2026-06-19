-- ====================================================================
-- TASK 2: PRODUCTION POSTGRESQL BUSINESS QUERIES
-- Target Table: amazon_sales
-- ====================================================================

-- Q1: Macro Financial Performance Metrics
SELECT 
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS total_gross_revenue,
    TO_CHAR(COUNT(DISTINCT order_id), 'FM999,999') AS total_unique_orders,
    TO_CHAR(SUM(total_sales_value) / COUNT(DISTINCT order_id), 'FM999.00 INR') AS average_order_value
FROM amazon_sales;

-- Q2: Top 5 Product Categories Ranked by Gross Revenue
SELECT 
    category,
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS category_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM amazon_sales
GROUP BY category
ORDER BY SUM(total_sales_value) DESC
LIMIT 5;

-- Q3: Revenue Split Proportion Between Fulfillment Route Models
SELECT 
    fulfilment,
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS fulfillment_revenue,
    ROUND((SUM(total_sales_value) * 100.0 / (SELECT SUM(total_sales_value) FROM amazon_sales))::numeric, 2) || '%' AS revenue_percentage
FROM amazon_sales
GROUP BY fulfilment;

-- Q4: Top 5 Indian Destination States by Revenue Traffic
SELECT 
    ship_state AS state,
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS state_revenue,
    COUNT(DISTINCT order_id) AS order_count
FROM amazon_sales
GROUP BY ship_state
ORDER BY SUM(total_sales_value) DESC
LIMIT 5;

-- Q5: B2B Commercial Accounts vs B2C Retail Consumer Profiles
SELECT 
    CASE WHEN b2b = true THEN 'B2B Commercial' ELSE 'B2C Retail' END AS customer_segment,
    COUNT(DISTINCT order_id) AS total_orders,
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS segment_revenue,
    TO_CHAR(AVG(total_sales_value), 'FM999.00 INR') AS average_order_value
FROM amazon_sales
GROUP BY b2b;

-- Q6: Order Urgency Impact on Transaction Basket Value
SELECT 
    order_urgency,
    COUNT(DISTINCT order_id) AS total_orders,
    TO_CHAR(SUM(total_sales_value), 'FM99,999,999.00 INR') AS urgency_revenue,
    TO_CHAR(AVG(total_sales_value), 'FM999.00 INR') AS average_basket_value
FROM amazon_sales
GROUP BY order_urgency
ORDER BY AVG(total_sales_value) DESC;
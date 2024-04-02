# Author: Sören Notredame

dropdown_query = "SELECT beerName, idName FROM brusselsbrews.beer;"
beers_query = "SELECT beerName, idName, beerText, allergens, image FROM brusselsbrews.beer;"

webshop_beers_query = "SELECT beerName, idName, beerText, bottlePrice, cratePrice, image FROM brusselsbrews.beer;"

webshop_insert_order = "INSERT INTO brusselsbrews.orders (name, total, date) VALUES (%s, %s, %s)"
webshop_insert_beers_order = "INSERT INTO brusselsbrews.order_beers (ordersID, beer, bottles, crates) VALUES (%s, %s, %s, %s)"

get_orders_id = "SELECT MAX(id) FROM brusselsbrews.orders where name = %s;"
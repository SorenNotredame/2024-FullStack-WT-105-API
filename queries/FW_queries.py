# Author: Frank Wagemans

insert_dealer_query = "INSERT INTO brusselsbrews.new_dealer (businessname, address, phone, email) VALUES (%s, %s, %s, %s);"

dealerinfo_query = "SELECT dealer.dealername, dealer.streetAndNumber, dealer.postal_codeAndCity, dealer.phone, dealer.email, dealer.opening_hours, GROUP_CONCAT(product.product_name) FROM brusselsbrews.dealer JOIN brusselsbrews.dealer_product ON dealer.dealer_id = dealer_product.dealer_id JOIN brusselsbrews.product ON dealer_product.product_id = product.product_id GROUP BY dealer.dealer_id;"

insert_tour_query = "INSERT INTO brusselsbrews.tour (name, email, phone, date, timeslot, amount) VALUES (%s, %s, %s, %s, %s, %s);"

insert_tasting_query = "INSERT INTO brusselsbrews.tasting (name, address, email, phone, date, amount) VALUES (%s, %s, %s, %s, %s, %s);"

brewerinfo_query = "SELECT brewername, streetAndNumber, postal_codeAndCity, phone, email, opening_hours, about FROM brusselsbrews.brewer;"

author_query = "SELECT authorname FROM brusselsbrews.author;"

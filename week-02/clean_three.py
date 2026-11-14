raw_a = " ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED"

parts_a = raw_a.split(";")
order_id_a = parts_a[0].upper().strip()
date_a = parts_a[1].strip()
customer_name_a = parts_a[2].title().strip()
items_name_a = parts_a[3].strip()
qty_a = int(parts_a[4])
price_a = float(parts_a[5].replace("৳", ""))
payment_a = parts_a[6].strip().lower()
status_a = parts_a[7].strip().lower()
unit_a = price_a / qty_a

print()
print(f"{order_id_a} . {date_a}")
print(f"{customer_name_a} purchased {items_name_a} - {qty_a}qty")
print(f"Total Price: ৳{price_a:.2f} (Unit Price: ৳{unit_a:.2f})")
print(f"Payment: {payment_a} . Status: {status_a}")

raw_b = "ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled"

parts_b = raw_b.split(";")
order_id_b = parts_b[0].strip()
date_b = parts_b[1].strip()
customer_name_b = parts_b[2].title().strip().replace("  ", " ")
items_name_b = parts_b[3].strip()
qty_b = int(parts_b[4])
price_b = float(parts_b[5].replace("৳" , "").replace("," , ""))
unit_b = price_b / qty_b
payment_b = parts_b[6].strip()
status_b =  parts_b[7].strip()

print()
print('"This order has been cancelled. Please do not count."') 
print(f"{order_id_b} . {date_b}")
print(f"{customer_name_b} purchased {items_name_b} - {qty_b}qty")
print(f"Total Price: ৳{price_b:.2f} (Per KG: ৳{unit_b:.2f})")
print(f"Payment: {payment_b} . Status: {status_b}")

raw_c = "ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered"

parts_c = raw_c.split(";")
order_id_c = parts_c[0].upper()
date_c = parts_c[1]
customer_name_c = parts_c[2].title().replace("  " , " ").strip()
items_name_c = parts_c[3]
qty_c = int(parts_c[4])
price_c = float(parts_c[5].replace("৳" , ""))
unit_c = price_c / qty_c
payment_c = parts_c[6].lower()
status_c = parts_c[7].lower()

print()
print(f"{order_id_c} . {date_c}")
print(f"{customer_name_c} purchased {items_name_c} - {qty_c}qty")
print(f"Total Price: ৳{price_c:.2f} (Unit Price: ৳{unit_c:.2f})")
print(f"Payment: {payment_c} . Status: {status_c}")
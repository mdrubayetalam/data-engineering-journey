raw_sales = """  ord100045 ; 2026-10-07 ;  RAHIM  uddin ; Miniket Chal 5kg ; 2 ; ৳ 1,240.50 ; BKASH ; delivered
ORD100046;2026-10-07;nusrat akter;Soybean Oil 2L;  1  ;৳350.00;nagad;delivered
  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED
ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled
ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered
  ORD100050 ;2026-10-09;  mim   begum ; Alu 2kg ; 2 ; ৳ 138.50 ; BKASH ;delivered
ord100051 ; 2026-10-10 ; FAHIM ahmed ; Chaa Pata 400g ; 1 ; ৳ 232.25 ; Rocket ; returned
ORD100052;2026-10-10;jannat  islam;Doodh 1L;  6  ; ৳ 558.00 ;nagad;delivered
  ord100053 ; 2026-10-11 ;  Sabbir   Rahman ; Peyaj 1kg ; 3 ;৳ 219.75; CASH ON DELIVERY ; delivered
ORD100054 ; 2026-10-11 ; afsana  chowdhury ; Apel 1kg ; 2 ; ৳ 1,105.00 ; bKash ; delivered"""

raw_sales_lines = raw_sales.strip().split("\n")

bkash_total = 0.0
nagad_total = 0.0
rocket_total = 0.0
cash_total = 0.0
card_total = 0.0

bkash_count = 0
nagad_count = 0
rocket_count = 0
cash_count = 0
card_count = 0

for raw_sale in raw_sales_lines:
    raw_sales_parts = raw_sale.split(";")
    payment_type = raw_sales_parts[-2].lower().strip()
    amount = float(raw_sales_parts[-3].replace("৳" , "").replace("," , ""))
    status = raw_sales_parts[-1].lower().strip()

    if status == "cancelled":
        continue

    if payment_type == "bkash":
       bkash_total += amount
       bkash_count += 1
    elif payment_type == "nagad":
         nagad_total += amount
         nagad_count += 1
    elif payment_type == "rocket":
         rocket_total += amount
         rocket_count += 1
    elif payment_type == "cash on delivery":
         cash_total += amount
         cash_count += 1
    elif payment_type == "card":
         card_total += amount
         card_count += 1

total = bkash_total + nagad_total + rocket_total + cash_total + card_total

print(f"bKash               {bkash_count} times    ৳{bkash_total:.2f}")
print(f"Nagad               {nagad_count} times    ৳{nagad_total:.2f}")
print(f"Rocket              {rocket_count} times    ৳{rocket_total:.2f}")
print(f"Cash on Delivery    {cash_count} times    ৳{cash_total:.2f}")
print(f"Card                {card_count} times    ৳{card_total:.2f}")
print()
print(f"Grand Total: ৳{total:.2f}")

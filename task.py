q_a=int(input("Enter the quantity of product A: "))
# price of product A
p_a=q_a * 20 
q_b=int(input("Enter the quantity of product B: "))
# price of product B
p_b=q_b * 40
q_c=int(input("Enter the quantity of product C: "))
# price of product C
p_c=q_c * 50

gift=int(input("whether the products are wrapped ? enter 1(if yes) and 2(if no)"))

total_quantity=q_a+q_b+q_c
cart_total =p_a + p_b + p_c

# output(1)
print("")
print("Results")
print("---------------")

print("Product A : Quantity= ",q_a,"units"," total amount= ",p_a)
print("Product B : Quantity= ",q_b,"units"," total amount= ",p_b)
print("Product C : Quantity= ",q_c,"units"," total amount= ",p_c)
# output(2)
print("")
print("Total amount for the 3 products= ",cart_total)

print("")


def flat_10_discount():
    if cart_total>200:
        amount1=cart_total-10
        return amount1
    else:
        return cart_total
    

def bulk_5_discount():
    p2_a=p_a
    p2_b=p_b
    p2_c=p_c
    if q_a>10:
        d2_a=(p_a*5)/100
        p2_a=p_a-d2_a
    if q_b>10:
        d2_b=(p_b*5)/100
        p2_b=p_b-d2_b
    if q_c>10:
        d2_c=(p_c*5)/100
        p2_c=p_c-d2_c
    amount2=p2_a+p2_b+p2_c
    return amount2
        
    

def bulk_10_discount():
    if total_quantity>20:
        discount3=(cart_total*10)/100
        amount3=cart_total-discount3
        return amount3
    else:
        return cart_total
    
def tiered_50_discount():
    if total_quantity>30:
        p4_a=p_a
        p4_b=p_b
        p4_c=p_c
        if q_a>15:
            d4_a=p_a/2
            p4_a=p_a-d4_a
        if q_b>15:
            d4_b=p_b/2
            p4_b=p_b-d4_b
        if q_c>15:
            d4_c=p_c/2
            p4_c=p_c-d4_c
        amount4=p4_a+p4_b+p4_c
        return amount4
    else:
        return cart_total
    
x=flat_10_discount()
y=bulk_5_discount()
z=bulk_10_discount()
u=tiered_50_discount()

l=[]
l.extend([x,y,z,u])

small=cart_total
for i in range(len(l)):
    if l[i]<small:
        small=l[i]
        index=i

# output(3)
s=small
if s==cart_total:
    print("No discount rule is applicable")
elif index==0:
    print("flat_10_discount is applied")
    discount=cart_total-s
    print("the discount amount is ",discount)
elif index==1:
    print("bulk_5_discount is applied")
    discount=cart_total-s
    print("the discount amount is ",discount)
elif index==2:
    print("bulk_10_discount is applied")
    discount=cart_total-s
    print("the discount amount is ",discount)
else:
    print("tiered_50_discount is applied")
    discount=cart_total-s
    print("the discount amount is ",discount)

# output(4)

package=total_quantity/10
shipping_fee=package * 5

if gift==1:
    gift_wrap_fee=total_quantity * 1
else:
    gift_wrap_fee=0
    
print("")
print("The total Shipping fee and gift wrap are")
print("Shipping fee= ",shipping_fee)
print("Gift wrap fee=",gift_wrap_fee)

# output(5)
print("")

total= s+shipping_fee+gift_wrap_fee
print("The total amount after applying discount rules and including shipping fee and gift wrap fee is ",total)
print("")









            


        


    














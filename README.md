# Marketplace.tf-Profit-Calculator
Originally used during Marketplace.tf's open period, this program was used to get the profit of items bought with keys and sold for dollars. Practically useless for me now, but can be used as an example of tkinter.

# Usage
The aim of the program is for you to buy keys with Marketplace.tf funds to purchase items with of which you will then sell on-site. The calculator can be used to calculate the profit you would get from doing this.

**Buy Price:** Input the price of the item you are buying. Key price can be decimal, and will be added to the ref price.
**Sell Price**: This is how many dollars the item will be sold for on Marketplace.tf
**Config**: Used to set current prices, it is EXTREMELY important these are accurate. Key price should reflect the price of keys on *Marketplace.tf* and ref value should represent how much keys are currently going for in refined on backpack.tf. *These values can be changed through* ***properties.txt,*** *where line 2 is key price and line 3 is ref value.*

**Uncle Discount:** Check this if the keys you have bought are affected by the uncle discount. Do not change key price if using this, as the discounted price will be shown. The discounted key price is given by ```(current key price [in dollars] * 10) / 11)``` as the function of uncle is giving you an extra key when you buy 10.

**Go:** With given values, this button will calculate the profit for you. Information will be displayed in the right panel.
**Reset:** This will reset every value and reload values from properties.txt

**Theme Selection:** Just a fun little experiment I added later on, allows you to change the colour of the program.

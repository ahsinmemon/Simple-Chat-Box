import random
from urllib import response

R_Eating = "I don't like eating anything because I'm a bot :)"
Q_Chick = """
Seven Things to Know When Caring for Baby Chicks

1. Be prepared before the chicks arrive.

Make sure you have a brooder area with a heat source prepared before chicks arrive. A brooder area is a contained area that provides a warm and safe environment for raising chicks.  Preparing this area 24 hours prior to chick arrival is best. Poultry brooders are available for purchase, or you can build your own brooder/brooder area. The brooder area is normally set up inside a barn, garage, or some type of enclosed building. 

2. Make sure you have the proper space.
overhead view of brooder area with lamp, litter, and baby chicks
This is an overhead view of a typical homemade brooder area. Young chicks require a heat source and room-temperature water along with pine shavings for bedding.

Try to provide .5 square foot per chick at the beginning.  Once the birds are fully mature, you will need between 2.5 to 3 square foot per bird if they are going to be confined and up to 10 square foot or more of outside space if ranging. Chickens are outside animals. They are not house pets. Some cities will allow chickens, and other cities may not.  Contact your city government to find out if your town allows chickens to be housed inside city limits. 

3. Choose the appropriate bedding or litter. 

Large pine shavings make good bedding or litter for baby chicks. Do not use small shavings or sawdust. Baby chicks learning to eat might eat the small shavings or sawdust, possibly causing an increase in mortality. Rice hulls, straw, or hay also make good bedding. Do not use sand or cedar shavings as it is not safe for the chicks.  You need to cover the entire brooder area with the bedding of your choice at approximately 1 to 3 inches deep.  On concrete floors use 3 to 5 inches of bedding. Turning the bedding/litter once per week will help it last longer. Pine shavings used for poultry bedding can be purchased at your local farm stores. 

4. Provide adequate heat for the chicks.
A drop light with a reflector shield is a good source of heat. Heat lamp bulbs that are 250 watts are ideal and will keep the birds comfortable. Red or white bulbs are available, and both are fine to use. You should hang the reflector light from something secure, so it does not come loose and drop down.  It could cause a fire or injure or kill the bird. The wattage of the bulb you are using will determine how high you will hang the light.

Place a thermometer at floor level to help ensure you have the proper temperature for the chicks, which should be around 95 degrees Fahrenheit for the first week.  The chicks will need enough space to move near the heat source or to walk away if too hot. The bottom of the bulb should be about 24 to 30 inches above the bedding.

5. The most important nutrient is water.
--Water should be at room temperature to prevent chicks from getting chilled while drinking.
--You should always have clean water available to the chicks.
--Upon the chicks’ arrival, be sure the water is at room temperature.
--Dip the beak of the chick in the water as you place them into the brooding area. The chicks will be thirsty when you get them.

Often baby chick mortality is caused because the chick doesn’t start to eat or drink.  Never let your chicks run out of water.  Occasionally chicks will get into the water, get wet and chilled. This can be prevented by using shallow water dispensers or placing marbles/tank rocks into the water foundation base to prevent chicks from submerging in the water.

6. Know how and what to feed your chicks.
Your feed trough should be low enough the chicks can see and reach the feed, even an open tray they can stand in is a good way to get them going.  Start your birds on chick starter, turkey starter or gamebird starter feed.  The high protein diet is best suited if you are wanting to develop a bird at its greatest potential.  You don’t need to add grit because the chick starter and grower feeds are formulated for what the chicks need to digest their food. Avoid feeding a scratch diet until the birds are fully matured. Chicks should stay on a starter or grower ration until they are 4 ½ to 5 months of age. Poultry feed can be purchased at your local farm stores.   

"""

def unknown():
    response['Could you please re-phrase that?',
             "...",
             "Sounds about right.",
             "What does that mean?"][random.randrange(4)]
    return response
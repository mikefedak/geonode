
#Add GeoDjango Module 
from django.contrib.gis.db import models 

#Input choices

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

# Shelter data models 

class Shelter_Details(models.Model):
	code = models.CharField("shelter key code", max_length=12, primary_key=True)
	name = models.CharField("Name of Shelter", max_length=70)
	ownership = models.CharField("Ownership Type", max_length=20)
	community = models.CharField("Community", max_length=30)
	recommendations = models.TextField("Final Recommendations")
	# ADD IN LOCATION FIELD AS POINT FIELD 

class Shelter_Contact(models.Model):
	code = models.ForeignKey(Shelter_Details, verbose name ="shelter key code",unique=True) #Link contact to details, it takes the PK by default
	manager = models.CharField("Shelter Manager", max_length=30)
	assistant = models.CharField("Assistant Manager", max_length=30)
	em_comm = models.CharField("Emergency Communication Capability", max_length=30)
	tel_num = models.BigIntegerField("Shelter Telephone Number")
	contact_p = models.CharField("Additional Contact Person", max_length=30)

class Manager_Contact(models.Model):
	manager = models.OneToOneField(Shelter_Contact, to_field="manager", related_name="shelter manager")
	tel_num = models.BigIntegerField("Shelter Manager Telephone Number")
	
class Assistant_Contact(models.Model):
	assistant = models.OneToOneField(Shelter_Contact, to_field="assistant", related_name="assistant shelter manager")
	tel_num = models.BigIntegerField("Assistant Manager Telephone Number")

class Contact_Person(models.Model):
	manager = models.OneToOneField(Shelter_Contact, to_field="contact_p", related_name="contact person")
	tel_num = models.BigIntegerField("Contact Person Telephone Number")
	
class Shelter_Structural(models.Model):
	#Choices lists, it would benice to get the local gov data so we could finalize the choices lists
	code = models.ForeignKey(Shelter_Details, verbose name ="shelter key code", unique=True) #Link contact to details, it takes the PK by default
	b_type = models.CharField("Primary Construction Material", max_length=15)
	num_floors = models.PositiveIntegerField("Number of Floors", max_value=6, min_value=1)
	occupied = models.CharField("Floors Occupied for Shelter", max length=50)
	sec_used = models.TextField("Sections of the Building to be used as a shelter")
	walls = models.BooleanField("Are all walls generally in good condition and free of large cracks", choices=BOOL_CHOICES)
 	windows = models.BooleanField("Are windows and glass doors protected by shutters", choices=BOOL_CHOICES)
	frames = models.BooleanField("Are frames (door/windows) properly affixed to walls", choices=BOOL_CHOICES)
	leaks = models.BooleanField("Is roof free of leaks", choices=BOOL_CHOICES)
	secured = models.BooleanField("Is the building secured", choices=BOOL_CHOICES)
	ceiling = models.BooleanField("Condition of Ceiling", choices=(('S', 'Satisfactory'),('US', 'Unsatisfactory')))
	damage_walls = models.CharField("Signs of damage or deterioration/cracks/holes to walls", max_length=30)
	damage_floors = models.CharField("Signs of damage or deterioration/cracks/holes to floors", max_length=30)
	ventilation = models.CharField("Ventilation", max_length=70)
	lighting = models.CharField("Lighting", max_length=70)
	pests = models.BooleanField("Is the building designed to minimise pests", choices=BOOL_CHOICES)
	ev_pests = models.BooleanField("Evidence of insects or rodents", choices=BOOL_CHOICES)
	ground_fl = models.BooleanField("Is the building's ground floor elevation on an equal or higher elevation than the ground level", choices=BOOL_CHOICES) 
	height_gf = models.PositiveIntegerField("Height of ground floor from ground level (feet)") 
	abv_gl = models.BooleanField("If multi-storied, does the building have a floor above the ground level suitable as shelter", choices=BOOL_CHOICES)
	roof_material = models.CharField("Roof Material", max_length=30)	
	roof_style = models.CharField("Roof Style", max_length=20)
	roof_pitch = models.CharField("Roof Pitch", max_length=20)
	window_type = models.CharField("Type of windows", max_length=50)
	open_blocks = models.BooleanField("Does any of the walls have open blocks", choices=BOOL_CHOICES)
	shutters = models.CharField("Do the windows have shutters", max_length=50)
	open_shutters = models.CharField("If yes, does the open blocks have shutters", max_length=20) 


class Shelter_Hazards(models.Model):
	flood_pot = models.BooleanField("Is the facility prone to flooding", choices=BOOL_CHOICES)
	com_flood = models.TextField("Comments on flooding potential")
	tsunami_r = models.CharField("Could the shelter be affected by storm surge or tsunami", choices=(('SS', 'Storm surge'),('TS', 'Tsunami')))
	code = models.ForeignKey(Shelter_Details, verbose name ="shelter key code", unique=True) #Link contact to details, it takes the PK by default
	struc_d = models.TextField("Damage to structure in the past 12-24months")
	haz_com = models.TextField("Comments on any porential hazards")
	past_events = models.TextField("Please list any past events that have impacted the shelter or community")

class  Shelter_Accessibility(models.Model):
	code = models.ForeignKey(Shelter_Details, verbose name ="shelter key code", unique=True) #Link contact to details, it takes the PK by default
	accessib = models.BooleanField("Is accessibility to the shelter easy", choices=BOOL_CHOICES)
	park_space = models.PositiveIntegerField("How many parking spaces are available on-site")
	exits = models.BooleanField("Are multiple entrances and exits available for persons in the shelter", choices=BOOL_CHOICES)
	upper_level = models.CharField("Access to upper level if identified as a shelter or post disaster shelter", max_length=50) 
 	ramp = models.CharField("Access ramp for building for disabled", max_length=30)
	capacity = models.PositiveIntegerField("Approximately how many people could sleep in the shelter")
	past_use = models.PositiveIntegerField("What is the maximum number of people who have used the shelter in the past 10 years in an event")

class Shelter_Amenities(models.Model):
	code = models.ForeignKey(Shelter_Details, verbose name ="shelter key code", unique=True) #Link contact to details, it takes the PK by default
	kitchen = models.BooleanField("Kitchen Facility", choices=BOOL_CHOICES)
	cooking_type = models.CharField("Type of Cooking Apparatus", max_length=30)
	other_storage = models.CharField("Other Storage Area", max_length=30)
	food_storage = models.CharField("Adequate and proper food storage area", max_length=30)
	laundry = models.CharField("Laundry area and facilities", max_length=20)
	yard = models.CharField("Condition of yard and surrounding", max_length=15, choices=(('SA', 'sanitary'),('US', 'unsanitary'))
	cond_yard = models.TextField("Recreation Area")
	num_restrooms = models.PositiveIntegerField("Number of Rest Rooms")
	num_male = models.PositiveIntegerField("Number of Male Toilets")
	num_female = models.PositiveIntegerField("Number of Female Toilets")
	num_uni = models.PositiveIntegerField("Number of Unisex Toilets")
	num_uri = models.PositiveIntegerField("Number of Urinals")
	loc_restrooms = models.CharField("Location of Rest Rooms", max_length=100)
	sat_restrooms = models.BooleanField("Are the Rest Rooms Satisfactory?", choices=BOOL_CHOICES)
	fun_restrooms = models.PositiveIntegerField("Are all of the toilets functional, if not how many are?")
	sewerage = models.CharField("Sewerage Disposal", max_length=100)
	comm_san = models.TextField("Any comments regarding sanitation")
	water_source = models.CharField("Water Sources", max_length=100)
	cistern_cap = models.PositiveIntegerField("Cistern capacity in gallons")
	filters = models.CharField("Are filters provided?", choices=(('Y', 'Yes'),('N', 'No'),('UK', 'Unknown'))
	onsite = models.BooleanField("Is the Cisten on site", choices-BOOL_CHOICES)
`	potable = models.CharField("Is there potable water?", max_length = 20)
	com_water = models.TextField("Any other comments about water available at shelter")
	power_a = models.CharField("Is there power supply (Mains)?", max_length=20)
	stan_pow = models.CharField("Is there stand-by power supply?", max_length=30)
	drop_off = models.BooleanField("Does the shelter have an identified or suitable drop-off location", choices=BOOL_CHOICES)
	supplies_sh = models.BooleanField("Is there an internal area within the building to store and secure supplies?
", choices=BOOL_CHOICES)
	sup_adq = models.BooleanField("If there is an internal storage area, is it adequate to store enough supplies for the shelter at maximum capacity
", choices=BOOL_CHOICES)
	
	

	




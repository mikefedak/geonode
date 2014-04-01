
#Add GeoDjango Module 
from django.contrib.gis.db import models  
#Non-spatial models  
#from django.db import models 
#Input choices

#BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

# Shelter data models 

class Shelter_Details(models.Model):
	code = models.CharField("shelter key code", max_length=12, primary_key=True)
	timestamp = models.DateField("Entry Date")
	name = models.CharField("Name of Shelter", max_length=70)
	institutio = models.CharField("Institution Type", max_length=50)
	owner = models.CharField("Ownership Type", max_length=50)
	community = models.CharField("Community", max_length=50)
	recommend = models.TextField("Final Recommendations")
	manager = models.CharField("Shelter Manager", max_length=50)
	assistant = models.CharField("Assistant Manager", max_length=50)
	em_comm = models.CharField("Emergency Communication Capability", max_length=100)
	tel_num = models.CharField("Shelter Telephone Number", max_length=50)
	contact_p = models.CharField("Additional Contact Person", max_length=50)
	man_tel_nu = models.CharField("Shelter Manager Telephone Number", max_length=50)
	man_tel_tw = models.CharField("Shelter Manager Phone 2", max_length=16 ) #Link contact to details, it takes the PK by default
	a_tel_num = models.CharField("Assistant Manager Telephone Number", max_length=50)
	cp_tel_num = models.CharField("Contact Person Telephone Number", max_length=50)
	b_type = models.CharField("Primary Construction Material", max_length=30)
	num_floors = models.CharField("Number of Floors", max_length=20)
	occupied = models.CharField("Floors Occupied for Shelter", max_length=50)
	sec_used = models.TextField("Sections of the Building to be used as a shelter")
	walls = models.CharField("Are all walls generally in good condition and free of large cracks", max_length=50)
 	win_shutte = models.CharField("Are windows and glass doors protected by shutters", max_length=5)
	frames = models.CharField("Are frames (door/windows) properly affixed to walls", max_length=5)
	leaks = models.CharField("Is roof free of leaks", max_length=50)
	secured = models.CharField("Is the building secured", max_length=5)
	ceiling = models.CharField("Condition of Ceiling", max_length=20, choices=(('S', 'Satisfactory'),('US', 'Unsatisfactory')))
	damage_wal = models.CharField("Signs of damage or deterioration/cracks/holes to walls", max_length=50)
	damage_flr = models.CharField("Signs of damage or deterioration/cracks/holes to floors", max_length=50)
	ventilatio = models.CharField("Ventilation", max_length=70)
	lighting = models.CharField("Lighting", max_length=70)
	pests = models.CharField("Is the building designed to minimise pests", max_length=5)
	ev_pests = models.CharField("Evidence of insects or rodents", max_length=5)
	ground_fl = models.CharField("Is the building's ground floor elevation on an equal or higher elevation than the ground level", max_length=5) 
	height_gf = models.IntegerField("Height of ground floor from ground level (feet)") 
	abv_gl = models.CharField("If multi-storied, does the building have a floor above the ground level suitable as shelter", max_length=5)
	roof_mat = models.CharField("Roof Material", max_length=50)	
	roof_style = models.CharField("Roof Style", max_length=20)
	roof_pitch = models.CharField("Roof Pitch", max_length=50)
	win_type = models.CharField("Type of windows", max_length=50)
	open_block = models.CharField("Does any of the walls have open blocks", max_length=5)
	shutters = models.CharField("Do the windows have shutters", max_length=50)
	open_shutt = models.CharField("If yes, does the open blocks have shutters", max_length=20) 
	flood_pot = models.CharField("Is the facility prone to flooding", max_length=5)
	damage_flo = models.CharField("Signs of Damage from Flooding", max_length=50) 
	com_flood = models.TextField("Comments on flooding potential")
	tsunami_r = models.CharField("Could the shelter be affected by storm surge or tsunami", max_length=40, choices=(('SS', 'Storm surge'),('TS', 'Tsunami')))
	struc_d = models.TextField("Damage to structure in the past 12-24months")
	mud_land_t = models.CharField("Is building or access to the building threatened by mudslides or landslides", max_length=5)
	lines_tree = models.CharField("Is building threatened by falling trees, boulders, power lines or flying debris", max_length=5)
	haz_mat = models.CharField("Is building located close to the source of any potential Hazardous materials", max_length=5)
	haz_com = models.TextField("Comments on any potential hazards")
	past_event = models.TextField("Please list any past events that have impacted the shelter or community")
	accessib = models.CharField("Is accessibility to the shelter easy", max_length=5)
	park_space = models.IntegerField("How many parking spaces are available on-site")
	exits = models.CharField("Are multiple entrances and exits available for persons in the shelter", max_length=5)
	upper_leve = models.CharField("Access to upper level if identified as a shelter or post disaster shelter", max_length=50) 
 	ramp = models.CharField("Access ramp for building for disabled", max_length=50)
	capacity = models.IntegerField("Approximately how many people could sleep in the shelter")
	past_use = models.IntegerField("What is the maximum number of people who have used the shelter in the past 10 years in an event")
	kitchen = models.CharField("Kitchen Facility", max_length=5)
	cooking_ty = models.CharField("Type of Cooking Apparatus", max_length=50)
	other_stor = models.CharField("Other Storage Area", max_length=50)
	food_stora = models.CharField("Adequate and proper food storage area", max_length=50)
	laundry = models.CharField("Laundry area and facilities", max_length=20)
	yard = models.CharField("Condition of yard and surrounding", max_length=20, choices=(('SA', 'sanitary'),('US', 'unsanitary')))
	rec_area = models.TextField("Recreation Area")
	nm_restroo = models.IntegerField("Number of Rest Rooms")
	num_male = models.IntegerField("Number of Male Toilets")
	num_female = models.IntegerField("Number of Female Toilets")
	num_uni = models.IntegerField("Number of Unisex Toilets")
	num_uri = models.IntegerField("Number of Urinals")
	loc_restrm = models.CharField("Location of Rest Rooms", max_length=100)
	restrm_con = models.CharField("Are the Rest Rooms Satisfactory?", max_length=5)
	toilet_fun = models.IntegerField("Are all of the toilets functional, if not how many are?")
	showers = models.IntegerField("Number of Showers")
	sewerage = models.CharField("Sewerage Disposal", max_length=100)
	com_san = models.TextField("Any comments regarding sanitation")
	water_sour = models.CharField("Water Sources", max_length=100)
	cistern_ca = models.IntegerField("Cistern capacity in gallons")
	cistern_se = models.CharField("Is the cistern adequately secured/protected", max_length=20)
	filters = models.CharField("Are filters provided?", max_length=20, choices=(('Y', 'Yes'),('N', 'No'),('UK', 'Unknown')))
	onsite = models.CharField("Is the Cisten on site", max_length=5)
	potable = models.CharField("Is there potable water?", max_length = 20)
	com_water = models.TextField("Any other comments about water available at shelter")
	power_a = models.CharField("Is there power supply (Mains)?", max_length=20)
	stan_pow = models.CharField("Is there stand-by power supply?", max_length=50)
	drop_off = models.CharField("Does the shelter have an identified or suitable drop-off location", max_length=5)
	supplies_s = models.CharField("Is there an internal area within the building to store and secure supplies?", max_length=5)
	sup_adq = models.CharField("If there is an internal storage area, is it adequate to store enough supplies for the shelter at maximum capacity", max_length=5)
	geom = models.PointField(srid=4326)
	objects = models.GeoManager()
	
	def __unicode__(self):
		return self.name

	
class Locations_2013(models.Model):
	Code = models.CharField("shelter key code", max_length=12, primary_key=True)
	Name = models.CharField("Shelter Name", max_length=254)
	Community = models.CharField("Community", max_length=50)
	Latitude = models.FloatField("Latitude")
	Longitude = models.FloatField("Longitude")
	geom = models.PointField(srid=4326)
	objects = models.GeoManager()

	
	




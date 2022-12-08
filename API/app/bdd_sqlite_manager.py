# Fichier - Classe - BddSQLiteManager

from sqlite3 import Error
from app.bdd_sqlite import BddSQLite

class BddSQLiteManager:

	# - - [Constructeur] - - - - - - - - - - - - - - - - - - - - -
	def __init__(self):
		# Init BDD
		self.bdd = BddSQLite()

		# Connexion BDD
		self.bdd.connection()

		# Initialisation de la BDD
		self.init()
	
	# - - [Initialisation de la BDD] - - - - - - - - - - - - - - - - - - - - -
	def init(self):

		# Vérification de la table bank_client dans la BDD
		try:
			table_bank_client = """
			CREATE TABLE IF NOT EXISTS 
				bank_client(
					id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
					d_age INT,
					d_marital INT,
					d_education INT,
					d_default INT,
					d_balance INT,
					d_housing INT,
					d_loan INT,
					d_month INT,
					d_duration INT,
					d_campaign INT,
					d_pdays INT,
					d_previous INT,
					d_poutcome INT,
					d_target INT
				)
			"""
			self.bdd.getExecute(table_bank_client)
			print("[BDD] Vérification de la table bank_client - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

		# Insertion des données la table bank_client de la BDD
		try:
			new_bank_client_1 = """INSERT INTO bank_client 
				(d_age, d_marital, d_education, d_default, d_balance, d_housing, d_loan, d_month, d_duration, d_campaign, d_pdays, d_previous, d_poutcome, d_target)
				VALUES
				(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			"""
			self.bdd.getExecute(new_bank_client_1)
			print("[BDD] Insertion dans la table bank_client - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

		# Lecture des données de la table bank_client de la BDD
		try:
			query = "SELECT * FROM bank_client"
			print(self.bdd.getAll(query))
			print("[BDD] Lecture de la table bank_client - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)
		
		# Lecture du dernier enregistrement de la table bank_client de la BDD
		try:
			result = self.getLastAddedBankClients()
			print(result)
			print("[BDD] Lecture du dernier enregistrement de la table bank_client - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

		# Lecture du nombre d'enregistrement de la table bank_client de la BDD
		try:
			result = self.getNumberBankClients()
			print(result)
			print("[BDD] Lecture du nombre d'enregistrement de la table bank_client - OK !")
		except Error as err:
			print('[BDD] Error !')
			print(err)

	# - - [Fonctions disponibles] - - - - - - - - - - - - - - - - - - - - -

	#Récupérationd de l'entité BDD
	def getBDD(self):
		return self.bdd
	
	#Récupération de la liste de données dans la table bank_client
	def getAllBankClients(self):
		query = "SELECT * FROM bank_client"
		result = self.getBDD().getAll(query=query)
		return result
	
	#Récupération d'une donnée dans la liste de données dans la table bank_client
	def getBankClients(self, id: int):
		query = "SELECT * FROM bank_client WHERE id = {}".format(id)
		# print(query, flush=True)
		result = self.getBDD().getOnce(query=query)
		return result
	
	#Récupération de la dernière données ajouté dans la liste de données dans la table bank_client
	def getLastAddedBankClients(self):
		query = "SELECT * FROM bank_client ORDER BY id DESC LIMIT 1"
		result = self.getBDD().getOnce(query=query)
		return result
	
	#Récupération du nombre de données de la liste de données dans la table bank_client
	def getNumberBankClients(self):
		query = "SELECT COUNT(*) as number FROM bank_client"
		result = self.getBDD().count(query=query)
		return result

	#Insertion d'une donnée dans la liste de données dans la table bank_client
	def insertBankClients(
		self,
		d_age:int, d_marital:int, d_education:int, d_default:int, d_balance:int, 
		d_housing:int, d_loan:int, d_month:int, d_duration:int, d_campaign:int, 
		d_pdays:int, d_previous:int, d_poutcome:int, d_target:int
		):
		query = """INSERT INTO bank_client
			(d_age, d_marital, d_education, d_default, d_balance, d_housing, d_loan, d_month, d_duration, d_campaign, d_pdays, d_previous, d_poutcome, d_target)
			VALUES
			({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
			""".format(
					d_age, d_marital, d_education, d_default, d_balance, 
					d_housing, d_loan, d_month, d_duration, d_campaign, 
					d_pdays, d_previous, d_poutcome, d_target
					)
		result = self.getBDD().getExecute(query=query)
		return result

	#Mise à jour d'une donnée dans la liste de données dans la table bank_client
	def updateBankClients(
		self, 
		id: int, 
		d_age:int, d_marital:int, d_education:int, d_default:int, d_balance:int, 
		d_housing:int, d_loan:int, d_month:int, d_duration:int, d_campaign:int, 
		d_pdays:int, d_previous:int, d_poutcome:int, d_target:int
		):
		query = """UPDATE bank_client
			SET 
			d_age = {}, d_marital = {}, d_education = {}, d_default = {}, d_balance = {}, d_housing = {}, d_loan = {}, 
			d_month = {}, d_duration = {}, d_campaign = {}, d_pdays = {}, d_previous = {}, d_poutcome = {}, d_target
			WHERE id = {}
			""".format(
				d_age, d_marital, d_education, d_default, d_balance, 
				d_housing, d_loan, d_month, d_duration, d_campaign, 
				d_pdays, d_previous, d_poutcome, d_target
				)
		result = self.getBDD().getExecute(query=query)
		return result

	#Suppresion d'une donnée dans la liste de données dans la table bank_client
	def deleteBankClients(self, id: int):
		query = """DELETE FROM bank_client WHERE id = {}""".format(id)
		result = self.getBDD().getExecute(query=query)
		return result

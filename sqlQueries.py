import sqlite3
conn = sqlite3.connect(‘flashcards.db’)
c = conn.cursor

def search_sets(username, searchTerm):
	searchResults = {}
	mySetsSearchQueryString = 
		"SELECT * from Uses u, Deck_owned_by_User du \
		WHERE du.user = u.deck_user \
		and du.title = u.deck_title \
		u.deck_title LIKE '\% %s \%' \
		or u.language_from like '\% %s \%' \
		or u.language_to like '\% %s \%' \
		or du.description like '\% %s \%' \
		and u.deck_user = '%s'"

	otherSetsSearchQueryString = 
		"SELECT * from Uses u, Deck_owned_by_User du \
		WHERE du.user = u.deck_user \
		and du.title = u.deck_title \
		u.deck_title LIKE '\% %s \%' \
		or u.language_from like '\% %s \%' \
		or u.language_to like '\% %s \%' \
		or du.description like '\% %s \%' \
		and u.deck_user <> '%s'"

	searchResults['mySets'] = c.execute(mySetsSearchQueryString % 
		(searchTerm, searchTerm, searchTerm, searchTerm, username)).fetch()
	searchResults['otherSets'] = c.execute(otherSetsSearchQueryString % 
		(searchTerm, searchTerm, searchTerm, searchTerm, username)).fetch()
	return searchResults

def add_other_user_set (setTitle, setUser, currUser):
	queryString = "INSERT INTO Adds VALUES(%s, %s, %s)"
	return c.execute(queryString % (currUser, setTitle, setUser))

def delete_Set(setTitle, setUser);
	queryString = "DELETE​​ FROM ​​Deck_owned_by_User ​deck WHERE​ deck​.user=​'%s' AND​​ deck​.​title​='%s'"
	return c.execute(queryString % (setUser, setTitle))	 

#
#	@author Andrea Tassotti

# Informazioni per la creazione del package
#
PACKAGE=pacchetto

# Aggiungere dipendenze e copiare i file necessari
all:	$(PACKAGE).spec 
	@cp -f dist/* tmp/
	@cd tmp; tar -czf /usr/src/redhat/SOURCES/$(PACKAGE).tar.gz *
	@rpm-build -a $(PACKAGE).spec
	@rm -f tmp/*

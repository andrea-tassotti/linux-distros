#
#	@author Andrea Tassotti
#
#	Necessario pacchetto: rpm-build rpmdevtools
#
#	Eseguire rpmdev-setuptree per creare nella home la struttura directory
#
#	Note: The above directory structure is for both CentOS and RedHat when using rpmbuild package. You can also use /usr/src/redhat directory, but you need to change the topdir parameter accordingly during the rpm build. If you are doing this on SuSE Enterprise Linux, use /usr/src/packages directory.
#

# Informazioni per la creazione del package
#
PACKAGE=pacchetto
#TOPDIR=/usr/src/redhat/
TOPDIR=/root/rpmbuild

# Aggiungere dipendenze e copiare i file necessari
all:	$(PACKAGE).spec 
	@mkdir -p tmp
	@cp -f dist/* tmp/
	@cd tmp; tar -czf $(TOPDIR)/SOURCES/$(PACKAGE).tar.gz *
	@rpmbuild -ba $(PACKAGE).spec
	@rm -f tmp/*

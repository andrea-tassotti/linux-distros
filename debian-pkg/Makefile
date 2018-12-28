#
# Dipende da dpkg-architecture e dpkg-deb
#
VERSION=0.0.0
SIZE=
PACKAGE_NAME=packagename
BUILDROOT=/tmp
PACKAGE_SOURCES=pkg
# Elencare con spazi e senza quotatura le cartelle preparate in BUILDROOT che si intende trasportare
ROOTS=usr
# Per eseguibili binari
ARCH=$(shell dpkg-architecture -qDEB_BUILD_ARCH 2>/dev/null)
# Per script
ARCH=all


build: prebuild
	@echo Building...
	dpkg-deb -b ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}
	@echo Moving package in current directory
	@mv /tmp/${PACKAGE_NAME}-${ARCH}-${VERSION}.deb .


# TODO: Aggiungere altre dipendenzea piacimento
prebuild: ${PACKAGE_SOURCES}/DEBIAN/control\
		${PACKAGE_SOURCES}/DEBIAN/preinst ${PACKAGE_SOURCES}/DEBIAN/prerm\
		${PACKAGE_SOURCES}/DEBIAN/postinst ${PACKAGE_SOURCES}/DEBIAN/postrm


	@echo Reconfiguring...
	@mkdir -p ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN
	@mkdir -p ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/usr/local
	# TODO: Creare directory necessarie

	@install --mode 755 ${PACKAGE_SOURCES}/DEBIAN/preinst ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/
	@install --mode 755 ${PACKAGE_SOURCES}/DEBIAN/prerm ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/
	@install --mode 755 ${PACKAGE_SOURCES}/DEBIAN/postinst ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/
	@install --mode 755 ${PACKAGE_SOURCES}/DEBIAN/postrm ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/
	# TODO: Aggiungere file da trasportare

	@cd ${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION} ; find ${ROOTS} -type f -exec md5sum '{}' \; >${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/md5sums

	@FILE=${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}
	@SIZE=`du -s ${FILE} | awk '{ print $$1 }'`; awk -vname=${PACKAGE_NAME} -vvers=${VERSION} -varch=${ARCH} -vsize=$$SIZE\
				    '/^Package:/{ print $$1" "name; next }\
				     /^Version:/{ print $$1" "vers; next }\
				     /^Installed-Size:/{ print $$1" "size; next }\
				     /^Architecture:/{ print $$1" "arch; next }\
					        { print $$0 }'\
			${PACKAGE_SOURCES}/DEBIAN/control >${BUILDROOT}/${PACKAGE_NAME}-${ARCH}-${VERSION}/DEBIAN/control



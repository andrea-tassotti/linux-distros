Summary: Sommario
Name: pacchetto
Version: 0.0.0
Release: 0
Vendor: Vendor
License: Copy
Group: Applications/Communications
Source: pacchetto.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
Requires: bash

%description
Descrizione estesa
e multilinea

%prep
%setup -c


%install
rm -rf $RPM_BUILD_ROOT
# TODO: Creare le directory di distribuzione
mkdir -p $RPM_BUILD_ROOT/usr/local/bin

# TODO: Installare quanto necessario
install provapacchetto	$RPM_BUILD_ROOT/usr/local/bin

%pre
if [ $1 -le 1 ]; then
# Normale prima istallazione
	echo Pre Prima installazione
else
# Aggiornamento
# Fermare i servizi coinvolti
	echo Aggiornamento
fi

%post
if [ $1 -le 1 ]; then
# Prima istallazione
# Configurare e avviare i servizi
	echo Post Prima installazione
fi

%preun
if [ $1 = 0 ]; then
# fermare e rimuovere i servizi
	echo Pre Uninstall
fi

%postun
if [ $1 = 0 ]; then
# Eliminazione del pacchetto
# cancellare eventuali gruppi e utenti
	echo Post uninstall: last
else
# Fine Aggiornamento con rimozione vecchio pacchetto
	echo Post uninstall: remove old
	# avviare servizi coinvolti
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /usr/local/bin/provapacchetto

%changelog
* Thu Dec 20 2018 Andrea Tassotti <root@localhost.localdomain>
- Aggiornamento va sopra
* Thu Dec 20 2018 Andrea Tassotti <root@localhost.localdomain>
- Versione iniziale 

Summary:	GtkSamba is a GUI tool to configure the SMB file server
Summary(pl):	Graficzne narzÍdzie do konfigurowania serwera plikÛw SMB
Name:		gtksamba
Version:	0.3.2pl1
Release:	1
License:	GPL
Vendor:		Perry Piplani <coder@open-systems.com>
Group:		X11/Applications/Networking
Group(cs):	X11/Aplikace/SÌªovÈ
Group(da):	X11/Programmer/NetvÊrks
Group(de):	X11/Applikationen/Netzwerkwesen
Group(es):	X11/Aplicaciones/Red
Group(fr):	X11/Applications/RÈseau
Group(is):	X11/Forrit/Net
Group(it):	X11/Applicazioni/Rete
Group(no):	X11/Applikasjoner/Nettverks
Group(pl):	X11/Aplikacje/Sieciowe
Group(pt_BR):	X11/AplicaÁıes/Rede
Group(pt):	X11/AplicaÁıes/Rede
Group(ru):	X11/“…Ãœ÷≈Œ…—/Û≈‘ÿ
Group(sl):	X11/Programi/Omreæni
Group(sv):	X11/Till‰mpningar/N‰tverk
Group(uk):	X11/“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ì≈“≈÷¡
URL:		http://www.open-systems.com/gtksamba.html
Source0:	ftp://ibiblio.org/pub/Linux/X11/gtkbuffet/apps/gtksamba/%{name}-%{version}.tar.gz
Patch0:		%{name}-smb.conf_path_fix.patch
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GtkSamba is a GUI tool for the Configuration of the Samba, the SMB
file server on X11/Unix. It will read, edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK
toolkit.

%description -l pl
GtkSamba jest narzÍdziem GUI s≥uø±cym do konfiguracji Samby, serwera
SMB na systemach uniksowych. Pozwala odczytaÊ, modyfikowaÊ i zapisaÊ
/etc/smb.conf, alternatywny plik konfiguracyjny lub dane z sieci.
Wykorzystuje bibliotekÍ GTK.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--without-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9ng README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gtksamba

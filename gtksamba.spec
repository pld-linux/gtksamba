Summary:	GtkSamba is a GUI tool to configure the SMB file server
Summary(pl):	Graficzne narzêdzie do konfigurowania serwera plików SMB
Name:		gtksamba
Version:	0.3.2pl1
Release:	2
License:	GPL
Vendor:		Perry Piplani <coder@open-systems.com>
Group:		X11/Applications/Networking
URL:		http://www.open-systems.com/gtksamba.html
Source0:	ftp://ibiblio.org/pub/Linux/X11/gtkbuffet/apps/gtksamba/%{name}-%{version}.tar.gz
# Source0-md5:	bd19a461d455b76764ac143d385d9f23
Patch0:		%{name}-smb.conf_path_fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GtkSamba is a GUI tool for the Configuration of the Samba, the SMB
file server on X11/Unix. It will read, edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK
toolkit.

%description -l pl
GtkSamba jest narzêdziem GUI s³u¿±cym do konfiguracji Samby, serwera
SMB na systemach uniksowych. Pozwala odczytaæ, modyfikowaæ i zapisaæ
/etc/smb.conf, alternatywny plik konfiguracyjny lub dane z sieci.
Wykorzystuje bibliotekê GTK.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{_bindir}/gtksamba

Summary:	GtkSamba is a GUI tool to configure the SMB file server
Summary(pl):	Graficzne narzêdzie do konfigurowania serwera plików SMB
Name:		gtksamba
Version:	0.3.2pl1
Release:	1
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
License:	GPL
URL:		http://www.open-systems.com/gtksamba.html
Vendor:		Perry Piplani <coder@open-systems.com>
Source0:	ftp://ibiblio.org/pub/Linux/X11/gtkbuffet/apps/gtksamba/%{name}-%{version}.tar.gz
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

%package static
Summary:	GtkSamba is a GUI tool to configure the SMB file server
Summary(pl):	Graficzne narzêdzie do konfigurowania serwera plików SMB
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe

%description static
GtkSamba is a GUI tool for the Configuration of the Samba, the SMB
file server on X11/Unix. It will read, edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK
toolkit.

%description static -l pl
GtkSamba jest narzêdziem GUI do konfigurowania Samby, serwera plików
SMB na X11/Uniksie. Czyta, edytuje i zapisuje /etc/smb.conf, plik
alternatywny b±d¼ z sieci. U¿ywa GTK.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix}/X11R6 \
	--without-gnome
%{__make} CC="%{__cc} -static %{rpmcflags}"
mv -f src/gtksamba src/gtksamba-static
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install src/gtksamba $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install src/gtksamba-static $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post static
if [ ! -e %{_prefix}/X11R6/bin/gtksamba ]; then
	cd %{_prefix}/X11R6/bin;
	ln -sf gtksamba-static gtksamba;
fi

%preun static
if [ -L %{_prefix}/X11R6/bin/gtksamba ]; then
	rm -f %{_prefix}/X11R6/bin/gtksamba;
fi

%files
%defattr(644,root,root,755)
%doc COPYING README TODO ChangeLog
%attr(755,root,root) %{_prefix}/X11R6/bin/gtksamba

%files static
%defattr(644,root,root,755)
%doc COPYING README TODO ChangeLog
%attr(755,root,root) %{_prefix}/X11R6/bin/gtksamba-static

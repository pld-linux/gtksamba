Summary:	GtkSamba is a GUI tool to configure the SMB file server.
Name:		gtksamba
Version:	0.3.2pl1
Release:	1
Group:		Applications/Networking
Copyright:	GPL
URL:		http://www.open-systems.com/gtksamba.html
Vendor:		Perry Piplani <coder@open-systems.com>
Source:		%{name}-%{version}.tar.gz
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSamba  is a GUI  tool for the  Configuration of  the Samba, the SMB
file server on  X11/Unix. It will read,  edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK toolkit.

%description -l pl
GtkSamba jest narzêdziem GUI s³u¿±cym do konfiguracji Samby, serwera SMB
na systemach uniksowych. Pozwala odczytaæ, modyfikowaæ i zapisaæ /etc/smb.conf,
alternatywny plik konfiguracyjny lub dane z sieci. Wykorzystuje bibliotekê GTK.

%package static
Summary:	GtkSamba is a GUI tool to configure the SMB file server.
Group:		Applications/Networking

%description static
GtkSamba is a GUI tool for the Configuration of the Samba, the SMB file
server on X11/Unix. It will read, edit and write /etc/smb.conf, an alternate
configuration file, or from a network. It uses the GTK toolkit.

%prep
%setup -q

%build
./configure \
	--prefix=/usr/X11R6 \
	--without-gnome
make CC="gcc -static $RPM_OPT_FLAGS"
mv src/gtksamba src/gtksamba-static
make CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -g 0 -o 0 -m 755 src/gtksamba $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -g 0 -o 0 -m 755 src/gtksamba-static $RPM_BUILD_ROOT/usr/X11R6/bin

%post static
if [ ! -e /usr/X11R6/bin/gtksamba ]; then
	cd /usr/X11R6/bin;
	ln -s gtksamba-static gtksamba;
fi

%preun static
if [ -L /usr/X11R6/bin/gtksamba ]; then
	rm /usr/X11R6/bin/gtksamba;
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README TODO ChangeLog
%attr(755,root,root) /usr/X11R6/bin/gtksamba

%files static
%doc COPYING README TODO ChangeLog
%attr(755,root,root) /usr/X11R6/bin/gtksamba-static

%define name gtksamba
%define version 0.3.2pl1
%define release 1

%define builddir /usr/src/redhat/BUILD/%{name}-%{version}

Summary: GtkSamba is a GUI tool to configure the SMB file server.
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Networking
Copyright: GPL
Packager: Ryan Weaver <ryanw@infohwy.com>
Url: http://www.open-systems.com/gtksamba.html
Vendor: Perry Piplani <coder@open-systems.com>
Distribution: Freshmeat RPMs
Source: %{name}-%{version}.tar.gz
Requires: samba
Buildroot: /tmp/%{name}-%{version}-%{release}-root

%description
GtkSamba  is a GUI  tool for the  Configuration of  the Samba, the SMB
file server on  X11/Unix. It will read,  edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK toolkit.

%package static
Summary: GtkSamba is a GUI tool to configure the SMB file server.
Group: Applications/Networking

%description static
GtkSamba  is a GUI  tool for the  Configuration of  the Samba, the SMB
file server on  X11/Unix. It will read,  edit and write /etc/smb.conf,
an alternate configuration file, or from a network. It uses the GTK toolkit.

*** STATICALLY COMPILED ***

%prep

%setup
./configure --prefix=/usr/X11R6 --without-gnome

%build
make CC="gcc -static $RPM_OPT_FLAGS"
mv src/gtksamba src/gtksamba-static
make CC="gcc $RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
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

%files
%doc COPYING README TODO ChangeLog
%attr(755,root,root) /usr/X11R6/bin/gtksamba

%files static
%doc COPYING README TODO ChangeLog
%attr(755,root,root) /usr/X11R6/bin/gtksamba-static

%clean
rm -r $RPM_BUILD_ROOT

%changelog
* Wed Jan 20 1999 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.3.2pl1-1]
- Version 0.3.2pl1 - 01/20/99	
- Fixed incompatibility with gtk+-1.0.6 and some 1.1.x versions.

* Wed Jan 20 1999 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.3.2-1]
- Version 0.3.2 - 01/20/99	
- Gnomified most of the dialog boxes, and improved them under Gtk.
- Gnomified part of the man page access, and added testparm and
  smbstatus to it.
- Included MANPATH search on search for man page
- Fixed paned window resize on main window resize.
- Misc. cleanup and fixes.

* Mon Jan  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.3.1-1]
- Version 0.3.1 - 01/03/99
- Now using both GNU autoconf and automake
- Optional support for Gnome is now included.
- Added capability to restart Samba
- Added support for preferences.
- Miscellaneous improvements.

* Sun Dec 27 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.3.0-1]
- Version 0.3.0 - 12/26/98
- Now using GNU autoconf.
- Incorporated a structure defining all parameter classes and types
  and added and dialog show all parameters available organized by type
- Added specialized dialogs for editing for inserting string, integer,
  octal and boolean type parameters, including checks for acceptable
  values.
- Incorporated patch from Pavel A. Sher <pavel@lime.hop.stu.neva.ru>
  adding support for gzipped man pages and latin character
  set. Thank you Pavel!!
- Included prompt when exiting via window manager.
- Updated the depricated menu factory to an item factory.
- Replaced the process of adding/removing clist widgets from a scrolled
  window when changing services to using a notebook with hidden tabs
  for the clist widgets
- Many miscellaneous fixes.
	
* Tue Dec  8 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.1.4-2]
- Split into 2 packages, 1 static, 1 dynamic.

* Mon Dec  7 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.1.4-1]
- Version 0.1.4 - 12/6/98
   Fixed incompatibility with gtk+-1.1.5
- Version 0.1.3 - 12/5/98
   Added interfaces to testparm and smbstatus
   Fixed case sensitivity in parameter lookup.

* Mon Nov 23 1998 Ryan Weaver <ryanw@infohwy.com>
  [gtksamba-0.1.2-1]
- Moved from using Fryguy_ to Ryan Weaver
- PGP signing RPMs
- Version 0.1.2 - 11/20/98
  - Added a help system that derives it's content from the smb.conf
    man page.

* Wed Nov 11 1998 Fryguy_ <fryguy@falsehope.com>
  [gtksamba-0.1.1-1]
- Version 0.1.1 - 11/10/98
  - Added dialogs for insert service, delete service, insert
    parameter, delete parameter and messages.
  - Added a toolbar
  - Updated the menus
  - Fixed seg-fault on closing a window when a dialog is open.

* Tue Nov 10 1998 Fryguy_ <fryguy@falsehope.com>
  [gtksamba-0.1.0-2]
- Passing $RPM_OPT_FLAGS to make via CC="gcc $RPM_OPT_FLAGS"

* Wed Nov  4 1998 Fryguy_ <fryguy@falsehope.com>
  [gtksamba-0.1.0-1]
- This is an early devlopment release, not all functionality is
  implemented. It will let you edit any existing parameter from a text
  entry, but without any checking.

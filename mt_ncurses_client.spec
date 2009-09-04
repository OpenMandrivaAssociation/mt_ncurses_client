%define name mt_ncurses_client
%define version 0.1.98
%define release %mkrel 6

Summary: A Maitretarot client base on ncurses
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glib2-devel ncurses-devel libmaitretarot-devel
BuildRequires: libmt_client-devel
Provides: maitretarot-client

%description
mt_ncurses_client is a Ncurses client for the Maitretarot server.
Maitretarot and its various clients make a Tarot game

%description -l fr
mt_ncurses_client est un client NCurses pour le serveur Maitretarot.
Maitretarot et ses differents clients constituent un jeu de tarot.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*



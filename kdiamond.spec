Name:		kdiamond
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kdiamond/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE desktop.

%files
%{_kde_bindir}/kdiamond
%{_kde_applicationsdir}/kdiamond.desktop
%{_kde_appsdir}/kdiamond
%{_kde_configdir}/kdiamond.knsrc
%{_kde_iconsdir}/*/*/*/kdiamond.*
%{_kde_docdir}/*/*/kdiamond
%{_kde_datadir}/sounds/KDiamond*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package


Name:		kdiamond
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kdiamond/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires: 	cmake(KF5NotifyConfig)

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
%cmake_kde5
%ninja -C build

%install
%ninja_install -C build



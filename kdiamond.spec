Name:		kdiamond
Version:	21.07.90
Release:	1
Epoch:		1
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kdiamond/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires: 	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5XmlGui)

%description
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE desktop.

%files -f kdiamond.lang
%{_datadir}/metainfo/org.kde.kdiamond.appdata.xml
%{_bindir}/kdiamond
%{_datadir}/knotifications5/kdiamond.notifyrc
%{_datadir}/applications/org.kde.kdiamond.desktop
%{_datadir}/kdiamond
%{_datadir}/knsrcfiles/kdiamond.knsrc
%{_iconsdir}/*/*/*/kdiamond.*
%{_datadir}/sounds/KDiamond*

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdiamond --with-html

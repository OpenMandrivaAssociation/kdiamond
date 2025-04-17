#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-kdiamond
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		https://www.kde.org/applications/games/kdiamond/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kdiamond/-/archive/%{gitbranch}/kdiamond-%{gitbranchd}.tar.bz2#/kdiamond-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdiamond-%{version}.tar.xz
%endif
BuildRequires:	cmake(KDEGames6)
BuildRequires: 	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6XmlGui)

%description
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE desktop.

%files -f kdiamond.lang
%{_datadir}/metainfo/org.kde.kdiamond.appdata.xml
%{_bindir}/kdiamond
%{_datadir}/knotifications6/kdiamond.notifyrc
%{_datadir}/applications/org.kde.kdiamond.desktop
%{_datadir}/kdiamond
%{_datadir}/knsrcfiles/kdiamond.knsrc
%{_iconsdir}/*/*/*/kdiamond.*
%{_datadir}/sounds/KDiamond*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdiamond-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdiamond --with-html

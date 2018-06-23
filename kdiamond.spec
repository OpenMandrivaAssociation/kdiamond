Name:		kdiamond
Version:	 18.04.2
Release:	1
Epoch:		1
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kdiamond/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires: 	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE desktop.

%files -f kdiamond.lang
%{_bindir}/kdiamond
%{_datadir}/knotifications5/kdiamond.notifyrc
%{_datadir}/applications/org.kde.kdiamond.desktop
%{_datadir}/kdiamond
%{_sysconfdir}/xdg/kdiamond.knsrc
%{_iconsdir}/*/*/*/kdiamond.*
%{_datadir}/sounds/KDiamond*
%{_datadir}/kxmlgui5/kdiamond/kdiamondui.rc

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdiamond --with-html

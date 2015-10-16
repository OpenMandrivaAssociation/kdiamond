Name:		kdiamond
Version:	15.08.2
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
%{_bindir}/kdiamond
%{_datadir}/knotifications5/kdiamond.notifyrc
%{_datadir}/applications/org.kde.kdiamond.desktop
%{_datadir}/kdiamond
%{_sysconfdir}/xdg/kdiamond.knsrc
%{_iconsdir}/*/*/*/kdiamond.*
%doc %{_docdir}/*/*/kdiamond
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



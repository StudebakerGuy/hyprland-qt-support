Name:		hyprland-qt-support
Version:	0.1.0
Release:	1
Source0:	https://github.com/hyprwm/hyprland-qt-support/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	A qt6 qml style provider for hypr* apps.
URL:		https://hyprland.org/
License:	GPL
Group:		System
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickControls2)
BuildSystem:	cmake
BuildOption:	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo
BuildOption:	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}
BuildOption:	-DINSTALL_QML_PREFIX=/%{_lib}/qt6/qml

%description
A qt6 qml style provider for hypr* apps.

%prep
%autosetup

%files
%{_libdir}/libhyprland-quick-styl*.so
%{_libdir}/qt6/qml/org/hyprland/style/*

%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		artikulate
Summary:	Artikulate
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	26f48d6b3c7947aa5ac4bfdb2871d02c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artikulate is a language learning application that helps improving
pronunciation skills for various languages. This repository maintains
the application and language specifications. All course files are
maintained in a separate repository named "artikulate-data" and hosted
on the KDE infrastructure.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/artikulate.knsrc
%attr(755,root,root) %{_bindir}/artikulate
%attr(755,root,root) %{_bindir}/artikulate_editor
%attr(755,root,root) %{_libdir}/libartikulatecore.so
%attr(755,root,root) %{_libdir}/libartikulatecore.so.0
%attr(755,root,root) %{_libdir}/libartikulatelearnerprofile.so
%attr(755,root,root) %{_libdir}/libartikulatelearnerprofile.so.0
%attr(755,root,root) %{_libdir}/libartikulatesound.so
%attr(755,root,root) %{_libdir}/libartikulatesound.so.0
%dir %{_libdir}/qt5/plugins/artikulate
%dir %{_libdir}/qt5/plugins/artikulate/libsound
%attr(755,root,root) %{_libdir}/qt5/plugins/artikulate/libsound/qtmultimediabackend.so
%{_desktopdir}/org.kde.artikulate.desktop
%{_datadir}/artikulate
%{_datadir}/config.kcfg/artikulate.kcfg
%{_iconsdir}/hicolor/16x16/actions/artikulate-course.png
%{_iconsdir}/hicolor/16x16/actions/artikulate-expression.png
%{_iconsdir}/hicolor/16x16/actions/artikulate-paragraph.png
%{_iconsdir}/hicolor/16x16/actions/artikulate-sentence.png
%{_iconsdir}/hicolor/16x16/actions/artikulate-word.png
%{_iconsdir}/hicolor/16x16/apps/artikulate.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-course-editor.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-course.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-expression.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-paragraph.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-sentence.png
%{_iconsdir}/hicolor/32x32/actions/artikulate-word.png
%{_iconsdir}/hicolor/32x32/apps/artikulate.png
%{_iconsdir}/hicolor/48x48/actions/artikulate-course.png
%{_iconsdir}/hicolor/48x48/actions/artikulate-expression.png
%{_iconsdir}/hicolor/48x48/actions/artikulate-paragraph.png
%{_iconsdir}/hicolor/48x48/actions/artikulate-sentence.png
%{_iconsdir}/hicolor/48x48/actions/artikulate-word.png
%{_iconsdir}/hicolor/48x48/apps/artikulate.png
%{_iconsdir}/hicolor/64x64/actions/artikulate-course-editor.png
%{_iconsdir}/hicolor/64x64/actions/artikulate-expression.png
%{_iconsdir}/hicolor/64x64/actions/artikulate-paragraph.png
%{_iconsdir}/hicolor/64x64/actions/artikulate-sentence.png
%{_iconsdir}/hicolor/64x64/actions/artikulate-word.png
%{_iconsdir}/hicolor/64x64/apps/artikulate.png
%{_iconsdir}/hicolor/scalable/actions/artikulate-course-editor.svgz
%{_iconsdir}/hicolor/scalable/actions/artikulate-expression.svgz
%{_iconsdir}/hicolor/scalable/actions/artikulate-paragraph.svgz
%{_iconsdir}/hicolor/scalable/actions/artikulate-sentence.svgz
%{_iconsdir}/hicolor/scalable/actions/artikulate-word.svgz
%{_iconsdir}/hicolor/scalable/actions/language-artikulate.svg
%{_iconsdir}/hicolor/scalable/apps/artikulate.svg
%{_datadir}/metainfo/org.kde.artikulate.appdata.xml

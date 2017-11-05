%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		artikulate
Summary:	Artikulate
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6d181f8b7bd9d9b82032b48cc4424dff
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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

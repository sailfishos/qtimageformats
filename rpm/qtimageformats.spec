Name:       qt5-qtimageformats
Summary:    Qt Imageformats
Version:    5.6.3
Release:    1%{?dist}
License:    LGPLv2 with exception or LGPLv3 or Qt Commercial
URL:        https://github.com/sailfishos/qtimageformats
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel >= 5.6.2
BuildRequires:  qt5-qtgui-devel
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Image Formats plugin

%package plugin-mng
Summary:    Qt Imageformats - MNG plugin

%description plugin-mng
This package provides the MNG imageformat plugin


%package plugin-tga
Summary:    Qt Imageformats - TGA plugin

%description plugin-tga
This package provides the TGA imageformat plugin


%package plugin-tiff
Summary:    Qt Imageformats - TIFF plugin

%description plugin-tiff
This package provides the TIFF imageformat plugin


%package plugin-wbmp
Summary:    Qt Imageformats - WBMP plugin

%description plugin-wbmp
This package provides the WBMP imageformat plugin


%package plugin-icns
Summary:    Qt Imageformats - ICNS plugin

%description plugin-icns
This package provides the ICNS imageformat plugin


%package plugin-webp
Summary:    Qt Imageformats - WEBP plugin

%description plugin-webp
This package provides the WEBP imageformat plugin


%prep
%setup -q -n %{name}-%{version}/qtimageformats

%build
export QTDIR=/usr/share/qt5
qmake -qt=5
make %{?_smp_flags}

%install
%qmake_install

# these manage to really royally screw up cmake
find %{buildroot}%{_libdir}/cmake/Qt5Gui/ -type f -name "*_*Plugin.cmake" \
-exec rm {} \;

%files plugin-mng
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqmng.so

%files plugin-tga
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqtga.so

%files plugin-tiff
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqtiff.so

%files plugin-wbmp
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqwbmp.so

%files plugin-icns
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqicns.so

%files plugin-webp
%defattr(-,root,root,-)
%license LICENSE.LGPLv21 LGPL_EXCEPTION.txt LICENSE.LGPLv3 LICENSE.GPLv3
%{_libdir}/qt5/plugins/imageformats/libqwebp.so

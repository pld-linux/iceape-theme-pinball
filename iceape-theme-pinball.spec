%define		_realname	pinball
%define		_snap		2007-02-02_sea1.1
Summary:	Great theme - it doesn't take much space
Summary(pl.UTF-8):	Przepiękny motyw - idealny kompromis pomiędzy rozmiarem i czytelnością
Name:		iceape-theme-pinball
Version:	2007.02.02
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozilla-themes.schellen.net/%{_realname}_%{_snap}.jar
# Source0-md5:	4e7575cbb285d341c10e1ff9dacc7f96
Source1:	gen-installed-chrome.sh
URL:		http://mozilla-themes.schellen.net/
Requires(post,postun):	iceape >= 1.1
Requires(post,postun):	textutils
Requires:	iceape >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/iceape/chrome

%description
The great theme, very good in low resolutions (800x600) - it doesn't
take much space, but it's still nice.

%description -l pl.UTF-8
Przepiękny motyw, który wyśmienicie nadaje się do używania w niskich
rozdzielczościach (800x600), gdyż zajmuje niewielką powierzchnię
ekranu nie tracąc przy tym na urodzie.

%prep
%setup -q -c -T
install %{SOURCE0} %{_realname}.jar
install %{SOURCE1} .
./gen-installed-chrome.sh skin %{_realname}.jar > %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/iceape-chrome+xpcom-generate

%postun
%{_sbindir}/iceape-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt

Summary:	Creates a pair of pseudo-terminals
Summary(pl):	Tworzy parê pseudo-terminali
Name:		pty-redir98
Version:	1.0
Release:	2
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://ftp.pld.org.pl/software/pty-redir98/%{name}-%{version}.tar.gz
# Source0-md5:	91c6d9069cbc4717d60c9c5a219cbe49
URL:		ftp://ftp.pld.org.pl/software/pty-redir98/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pty-redir98 is a remake of old "pty-redir" application, using Unix98
PTYs. It creates a pair of pseudo-terminals for any application to
use. For example it allows running PPP over SSH by attaching SSH
input/output to a pseudo-tty master and running pppd on corresponding
slave.

%description -l pl
pty-redir98 jest przeróbk± starego programu "pty-redir", u¿ywaj±c±
pseudo-terminali zgodnie z semantyk± Unix98. Tworzy parê
pseudo-terminali które dowolna aplikacja mo¿e wykorzystaæ. Na przyk³ad
umo¿liwia uruchomienie PPP po SSH przez podczepienie wej¶cia/wyj¶cia
SSH do nadrzêdnego pseudo-terminala i uruchomienie pppd na
odpowiadaj±cym mu pseudo-terminalu podrzêdnym.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/%{name}

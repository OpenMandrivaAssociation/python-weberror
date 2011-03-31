%define tarname	WebError
%define name	python-weberror
%define version 0.10.3
%define release %mkrel 1

Summary:	Web error handling and exception catching for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/WebError/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-tempita, python-webob, python-pygments
Requires:	python-paste >= 1.7.1
BuildRequires:	python-setuptools

%description 
This package provides Python libraries for web error handling and
exception catching.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE


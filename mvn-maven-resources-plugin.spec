#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-resources-plugin
Version  : 2.7
Release  : 5
URL      : https://github.com/apache/maven-resources-plugin/archive/maven-resources-plugin-2.7.tar.gz
Source0  : https://github.com/apache/maven-resources-plugin/archive/maven-resources-plugin-2.7.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.jar
Source8  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.jar
Source10  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-resources-plugin-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-resources-plugin package.
Group: Data

%description data
data components for the mvn-maven-resources-plugin package.


%prep
%setup -q -n maven-resources-plugin-maven-resources-plugin-2.7

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.6/maven-resources-plugin-2.6.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/2.7/maven-resources-plugin-2.7.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.1/maven-resources-plugin-3.0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.0.2/maven-resources-plugin-3.0.2.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.pom

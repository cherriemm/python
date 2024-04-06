# Introduction to XML



XML is a software and hardware independent tool for storing and transporting data.

- stand for eXtensible Markup Language

- a markup language much like HTML

- self-descriptive

  

**difference between XML and HTML**

- XML was designed to carry data - with focus on what data is
- HTML was designed to display data -with focus on how data looks
- XML tags are not predefined like HTML tags are, with XML the author must define both the tags and the document structure.



**advance of XML**

- XML simplifies data sharing
- XML simplifies data transport
- XML simplifies platform changes
- XML simplifies data availability

Many computer systems contain data in incompatible formats. Exchanging data between incompatible systems (or upgraded systems) is a time-consuming task for web developers. Large amounts of data must be converted, and incompatible data is often lost.

XML stores data in plain text format. This provides a software- and hardware-independent way of storing, transporting, and sharing data.



## **How can XML be used ?**

**Separate data from presentation**

XML does not carry any information about how to be displayed.

The same XML data can be used in many different presentation scenarios.

Since XML tags are "invented" by the author of the XML document, browsers do not know if a tag like <table> describes an HTML table or a dining table.

Without any information about how to display the data, the browsers can just display the XML document as it is.





**Often a complement to HTML**

In many  HTML applications, XML is used to store or transport data, while HTML is used to format and display the same data.



**Separate data from HTML**

When displaying data in HTML, you should not have to edit the HTML file when the data changes.

With XML, the data can be stored in separate XML files.

With a few lines of JavaScript code, you can read an XML file and update the data content of any HTML page.



**transaction data**

Thousands of XML formats exist, in many different industries, to describe day-to-day data transactions:

- Stocks and Shares
- Financial transactions
- Medical data
- Mathematical data
- Scientific measurements
- News information
- Weather services

Using a standard makes it easier for both news producers and news consumers to produce, receive, and archive any kind of news information across different hardware, software, and programming languages.





## XML Tree

![image-20240406164122220](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240406164122220.png)

```xml
<?xml verison="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italians</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>

    <book category="child">
        <title lang="en">Harry Potter</title>
        <author>J K . Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    
    <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>
```



#### XML Element

everything from (including) the element's start tag to (including) the element's end tag

`<price>29.99</price>`

An element can contain:

- text
- attributes
- other elements
- or a mix of the above



#### XML Attributes

Some things to consider when using attributes are:

- attributes cannot contain multiple values (elements can)
- attributes cannot contain tree structures (elements can)
- attributes are not easily expandable (for future changes)



#### XML Namespaces

provide a method to avoid element name conflicts.



**Name conflicts**

In XML, element names are defined by the developer. This often results in a conflict when trying to mix XML documents from different XML applications

![image-20240406180455696](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240406180455696.png)



**Solving the name conflict using a prefix**

when using prefixes in XML, a namespace for the prefix must be defined:

- defined by an `xmlns` attribute in the start tag of an element.

  ```xml
  <root>
  
  <h:table xmlns:h="http://www.w3.org/TR/html4/">
    <h:tr>
      <h:td>Apples</h:td>
      <h:td>Bananas</h:td>
    </h:tr>
  </h:table>
  
  <f:table xmlns:f="https://www.w3schools.com/furniture">
    <f:name>African Coffee Table</f:name>
    <f:width>80</f:width>
    <f:length>120</f:length>
  </f:table>
  
  </root>
  ```

-  also be declared in the XML root element:`<root xmlns:h="http://www.w3.org/TR/html4/"
  xmlns:f="https://www.w3schools.com/furniture">`

**Note:** 

The purpose of using an URI is to give the namespace a unique name , not used by the parser to look up information.

However, companies often use the namespace as a pointer to a web page containing namespace information.



**URI : Uniform Resource Identifier**

A URI is a string of characters which identifies an Internet Resource .

The most common URI is the **Uniform Resource Locator (URL)** which identifies an Internet domain address. 

Another not so common type of URI is the **Uniform Resource Name** (URN).





**Default Namespaces**

Defining a default namespace for an element saves us from using prefixes in all the child elements. 

`xmlns="namespaceURI"`









## XML syntax Rules



- **XML Documents must have a root element**

```xml
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```



- **prolog**

The XML prolog is optional. If it exists, it must come first in the document.

UTF-8 is the default character encoding for XML documents.

A prolog defines the XML version and the character encoding:

```
<?xml version="1.0" encoding="UTF-8"?>
```

![image-20240406165414082](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240406165414082.png)



- **All XML elements must have a closing tag**

  **Note:** The XML prolog does not have a closing tag! This is not an error. The prolog is not a part of the XML document.



- **Naming rules**

  -  case-sensitive

  - Element names must start with a letter or underscore

  - Element names cannot start with the letters xml (or XML, or Xml, etc)

    Any name can be used, no words are reserved (except xml)

  - Element names can contain letters, digits, hyphens, underscores, and periods

     cannot contain spaces

  **Attention**

  Avoid "-". If you name something "first-name", some software may think you want to subtract "name" from "first".

  Avoid ".". If you name something "first.name", some software may think that "name" is a property of the object "first".

  Avoid ":". Colons are reserved for namespaces (more later).

  Non-English letters like éòá are perfectly legal in XML, but watch out for problems if your software doesn't support them!



- **XML Attributes values must always be quoted**

  XML element can have attributes in name/value pairs just like in HTML and the attribute values must always be quoted. either single or double quotes

  If the attribute value itself contains double quotes you can use single quotes  `<gangster name='George "Shotgun" Ziegler'>`

  or use character entities : `<gangster name="George &quot;Shotgun&quot; Ziegler">`

  



- **Entity References**

  If you place a character like "<" inside an XML element, it will generate an error because the parser interprets it as the start of a new element.

  5 pre-defined entity references in XML:

  | `&lt`   | <    | less than      |
  | ------- | ---- | -------------- |
  | `&gt`   | >    | greater than   |
  | `&amp`  | &    | ampersand      |
  | `&apos` | '    | apostrophe     |
  | `&quot` | "    | quotation mark |



- **Comments** 

  `<!-- This is a comment --!>`



- **White-space is preserved in XML**

  | XML:  | Hello      Tove |
  | ----- | --------------- |
  | HTML: | Hello Tove      |



- XML stores new line as LF

  Windows applications store a new line as: carriage return and line feed (CR+LF).

  Unix and Mac OSX use LF.

  Old Mac systems use CR.

  XML stores a new line as LF.





# XML HttpRequest

all modern browsers have a buit-in XMLHttpRequest object to request data from a server .
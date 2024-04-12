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



**Empty XML Elements**

An element with no content is said to be empty.

indicate an empty  element like :

```xml
<element></element>
or
<element/>
```









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



# Usage



## XML Parser

Before an XML document can be accessed, it must be loaded into an XML DOM object .

All modern browsers have a built-in XML parser that can convert text into an XML DOM object

The XML DOM (document object model) defines the properties and methods for accessing and editing XML . 







## XML HttpRequest

all modern browsers have a built-in XMLHttpRequest object to request data from a server .

- Update a web page without reloading the page
- Request/receive data from a server - after the page has loaded
- Send data to a server - in the background



### XML HttpRequest example



A common JavaScript syntax for using the XMLHttpRequest object :

```js
var xthhp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if(this,readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready
        document,getElementById("demo").innerHTML = xhttp.responseText;
    }
};
xhttp.open("GET", "filename", true)
xhttp.send();


// the onreadystatechange property specifies a function to be executed every time the status of the XMLHttpRequest object changes
```





















# XML in python

https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.text

First import `xml.etree.ElementTree` 

```xml
import xml.etree.ElementTree as ET
```

`ET` has two classes for this purpose - [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) represents the whole XML document as a tree, and [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) represents a single node in this tree. Interactions with the whole document (reading and writing to/from files) are usually done on the `ElementTree` level. Interactions with a single XML element and its sub-elements are done on the Element level.



## ElementTree Objects

`class xml.etree.ElementTree.ElementTree(element=None, file=None)`

*element*  :  the root element. 

The tree is initialized with the contents of the XML *file* if given.

ElementTree wrapper class. This class represents an entire element hierarchy, and adds some extra support for serialization to and from standard XML.







`xml.etree.ElementTree.SubElement(parent, tag, attrib={}, extra)`

子元素工厂函数。 这个函数会创建一个元素实例，并将其添加到现有的元素。

元素名、属性名和属性值可以是字节串或 Unicode 字符串。

 *parent* :父元素 

*tag*  : 子元素名。 

*attrib*  :一个可选的字典，其中包含元素属性。

*extra* 包含额外的属性，以关键字参数形式给出。 

返回一个元素实例。



#### `iter(tag=None)`

Creates and returns a tree iterator for the root element. The iterator loops over all elements in this tree, in section order. *tag* is the tag to look for (default is to return all elements).





## Element Object



#### `Element(tag, attrib={}, extra)`

`class xml.etree.ElementTree.Element(tag, attrib={}, extra)`

- *tag*  :  the element name

- *attrib* : an optional dictionary, containing element attributes. 

- *extra*  : contains additional attributes, given as keyword arguments.



- text, tail

  These attributes can be used to hold additional data associated with the element. Their values are usually strings but may be any application-specific object.

  the *text* attribute holds either the text between the element’s start tag and its first child or end tag, or None



Attention :

![image-20240407121121111](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240407121121111.png)


You have to be careful with the word "attribute", as that can refer to 2 things here. `extra` is for setting XML element attributes that appear as attributes in your XML element open tag. The Python object you create with Element() has got a **Python instance attribute** `text` that you can use to set the text inside your XML element. However, that text is not an XML element attribute.







**The following dictionary-like methods work on the element attributes.**

- `set(key, value)`

  set the attribute key on the element to value



- `get(key, default=None)`

  Gets the element attribute named *key*.

  Returns the attribute value, or *default* if the attribute was not found.



- `items()`

  Returns the element attributes as a sequence of (name, value) pairs. The attributes are returned in an arbitrary order.



**The following methods work on the element’s children (subelements)**



#### `append(subelement)`

Adds the element *subelement* to the end of this element’s internal list of subelements. Raises 	`TypeError` if subelement is not an Element



#### `insert(index)`





#### `iter(tag=None)`

create a tree iterator with the current element as the root . 

The iterator iterates over this element and all elements below it, in document (depth first) order

 If *tag* is not `None` or `'*'`, only elements whose tag equals *tag* are returned from the iterator. If the tree structure is modified during iteration, the result is undefined.

```python
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
    
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}
```





#### `find(match, namespaces=None)`

Find the first subelement matching match .

match may be a tag name or a path . Returns an element instance or None.





#### `iterfind(match, namespaces=None)`

Finds all matching subelements, by tag name or [path](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath). Returns an iterable yielding all matching elements in document order. *namespaces* is an optional mapping from namespace prefix to full name.









## Functions



### indent

- `xml.etree.ElementTree.indent(tree, space=' ', level=0)`

Appends whitespace to the subtree to indent the tree visually. This can be used to generate pretty-printed XML output. 

*tree* can be an Element or ElementTree. 

*space* is the whitespace string that will be inserted for each indentation level, two space characters by default. 

For indenting partial subtrees inside of an already indented tree, pass the initial indentation level as *level*.





### parsing XML

import XML data by reading from a file or directly from a string :

```python
import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

# or
root = ET.fromstring(country_data_as_string)
```



- `fromstring` parses XML from a string directly into an `Element` : the root of the parsed tree . Other parsing functions may create an `ElementTree` , check the documentation to be sure .

As an `Element` , root has a tag and a dictionary of attributes , also has children nodes over which we can iterate

```python
>>> root.tag
'data'
>>>root.attrib
{}

>>> for child in root:
    	print(child.tag, chid.attrib)
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
```

children are nested, and we can access specific child nodes by index:

```python
>>> root[0][1].text
```








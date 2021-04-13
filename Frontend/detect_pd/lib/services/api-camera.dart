import 'dart:convert';
import 'dart:io';
import 'package:detect_pd/views/ui/loading-screen.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:dropdownfield/dropdownfield.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/main.dart';
import 'package:detect_pd/views/ui/neg-results-page.dart';
import 'package:detect_pd/views/ui/pos-result-page.dart';
import 'package:detect_pd/views/ui/settings-page.dart';

class CameraAccess extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => CameraAccessState();
}

class CameraAccessState extends State<CameraAccess> {
  File galleryFile;
  File image;
  final picker = ImagePicker();
  final TextEditingController ageController = TextEditingController();
  String gender;
  List genders = ["Male", "Female"];
  String handedness;
  List handednessList = ["Right-handed", "Left-handed"];
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  Future<dynamic> pickImageFromGallery(ImageSource source) async {
    /// This method will select image from given source using ImagePicker()
    final image = await picker.getImage(source: source);

    // set image uploaded as image variable declared at class level
    setState(() {
      this.image = File(image.path);
    });
  }

  Future doUpload() async {
    /// This method will send requests to API at specified host address
    try {
      // request uri (uniform resource identifier)
      var request = http.MultipartRequest('POST', Uri.parse("http://detectpd.us-east-2.elasticbeanstalk.com/create_user"));

      // creating request.fields
      request.fields['age'] = ageController.text;

      // conditional block to check if user entered gender is male or female
      // if male then assign request field as 1, else as 2
      if (gender == "Male"){
        request.fields['gender'] = "1";
      } else {
        request.fields['gender'] = "2";
      }

      if (handedness == "Right-handed"){
        request.fields['handedness'] = "1";
      } else {
        request.fields['handedness'] = "2";
      }

      // Map data structure used for to create request headers
      Map<String, String> headers = {"Content-type": "multipart/form-data", 'connection': 'keep-alive'};

      // MultipartFile : define media type as image(jpg)
      request.files.add(
        http.MultipartFile(
          'image',
          image.readAsBytes().asStream(),
          image.lengthSync(),
          filename: "filename",
          contentType: MediaType('image', 'jpg'),
        ), // http.MultipartFile
      );

      // adding request headers
      request.headers.addAll(headers);
      print("request: " + request.toString());

      // mount loading screen using Navigator class
      Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => (LoadingPage()))
      );

      // send http POST request
      final resp = await request.send();
      print(resp.statusCode);
      String respStr = await resp.stream.bytesToString();
      print(respStr);

      // decode backend response from POST request
      final decodeRespStr = json.decode(respStr) as Map<String, dynamic>;
      int imageNo = decodeRespStr['image_no'];

      //async function to perform http GET
      final response = await http.get('http://detectpd.us-east-2.elasticbeanstalk.com/retrieve_result?image_no=$imageNo'); //getting the response from our backend server script

      final decoded = json.decode(response.body) as Map<String, dynamic>; //converting it from json to key value pair

      if (decoded['result'] == false) {
        // display positive results page
        Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context) => PositiveResultsPage()));
      } else {
        // display negative results page
        Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context) => NegativeResultsPage()));
      }

    } catch (exception) {
        print("ERROR OCCURRED");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Container(
        padding: EdgeInsets.all(32),
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.only(
                  bottom: 35,
                ), // EdgeInsets.only
                child: Text(
                  "Enter the following",
                  style: TextStyle(
                    fontSize: 20,
                    color: const Color(0xFF033E6B),
                  ), // TextStyle
                ), // Text
              ), // Padding
              Container(
                height: 70.0,
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                ), // BoxDecoration
                child: TextFormField(
                  controller: ageController,
                  keyboardType: TextInputType.number,
                  decoration: new InputDecoration(
                    labelText: 'Age',
                    contentPadding: EdgeInsets.all(2.0),
                    focusedBorder: InputBorder.none,
                    enabledBorder: InputBorder.none,
                    labelStyle: TextStyle(color: const Color(0xFF033E6B), fontSize: 18),
                    icon: Icon(Icons.add),
                  ), // InputDecoration
                  autovalidateMode: AutovalidateMode.always,
                  // validator function
                  validator: (value) {
                    if(value.isEmpty){
                      return 'Age Required';
                    }
                    return null;
                  },
                ), // TextField
              ), // Container
              Container(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Container(
                  width: 320.0,
                  height: 60.0,
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  margin: EdgeInsets.only(bottom: 5.0),
                  decoration: BoxDecoration(
                    color: Color.fromRGBO(118, 176, 195, 100),
                    borderRadius: BorderRadius.circular(10),
                  ), // BoxDecoration
                  child: DropdownButton(
                    isExpanded: true,
                    hint: Text("Gender"),
                    dropdownColor: Colors.teal[200],
                    style: TextStyle(
                      color: const Color(0xFF033E6B),
                      fontSize: 18,
                    ), // TextStyle
                    value: gender,
                    onChanged: (newValue) {
                      setState(() {
                        gender = newValue;
                      });
                    },
                    items: genders.map((valueItem){
                      return DropdownMenuItem(
                        value: valueItem,
                        child: Text(valueItem),
                      ); // DropdownMenuItem
                    }).toList(),
                    iconSize: 36,
                    underline: SizedBox(),
                  ), // DropDownButton
                ), // Container
              ), // Container
              Container(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                margin: EdgeInsets.only(bottom: 5.0),
                decoration: BoxDecoration(
                  color: Color.fromRGBO(118, 176, 195, 100),
                  borderRadius: BorderRadius.circular(10),
                ), // BoxDecoration
                child: Container(
                  width: 320.0,
                  height: 60.0,
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  margin: EdgeInsets.only(bottom: 5.0),
                  decoration: BoxDecoration(
                      color: Color.fromRGBO(118, 176, 195, 100),
                      borderRadius: BorderRadius.circular(10)), // BoxDecoration
                  child: DropdownButton(
                    isExpanded: true,
                    hint: Text("Handedness"),
                    dropdownColor: Colors.teal[200],
                    style: TextStyle(
                      color: const Color(0xFF033E6B),
                      fontSize: 18,
                    ), // TextStyle
                    value: handedness,
                    onChanged: (newValue) {
                      setState(() {
                        handedness = newValue;
                      });
                    },
                    items: handednessList.map((valueItem){
                      return DropdownMenuItem(
                        value: valueItem,
                        child: Text(valueItem),
                      ); // DropDownMenuItem
                    }).toList(),
                    iconSize: 36,
                    underline: SizedBox(),
                  ), // DropDownButton
                ), // Container
              ), // Container
              Padding(
                padding: EdgeInsets.all(10.0),
                child: RaisedButton(
                  child: new Text('Take photo from camera'),
                  color: Colors.grey[400],
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(18.0),
                  ), // RoundedRectangularBorder
                  onPressed: () => pickImageFromGallery(ImageSource.camera),
                ), // RaisedButton
              ), // Padding
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: SizedBox(
                  child: image == null
                      ? Center(child: new Text('Image Required', style: TextStyle(color: Colors.red[400]),))
                      : Center(child: new Image.file(image)),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: FloatingActionButton(
                  onPressed: () {
                    if(!_formKey.currentState.validate()){
                      print("Invalid Submission");
                      _formKey.currentState.reset();
                    } else {
                      _formKey.currentState.save();
                      doUpload();
                    }
                  },
                  child: Icon(Icons.add),
                  backgroundColor: Colors.teal,
                ),
              ), // SizedBox
            ], // <Widget>[]
          ), // Column
        ), // SingleChildScrollView
      ), // Container
    ); // Scaffold
  }
}

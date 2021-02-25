import 'dart:convert';

TesterModel testerModelFromJson(String str) => TesterModel.fromJson(json.decode(str));
String testerModelToJson(TesterModel data) => json.encode(data.toJson());

class TesterModel {
  TesterModel({
    this.age,
    this.gender,
    this.handedness,
  });

  String age;
  String gender;
  String handedness;

  factory TesterModel.fromJson(Map<String, dynamic> json) => TesterModel(
    age: json["age"],
    gender: json["gender"],
    handedness: json["handedness"],
  );

  Map<String, dynamic> toJson() => {
    "age": age,
    "gender": gender,
    "handedness": handedness,
  };
}

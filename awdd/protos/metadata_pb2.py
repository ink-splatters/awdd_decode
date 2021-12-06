# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import type_pb2 as google_dot_protobuf_dot_type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/metadata.proto',
  package='awdd.metadata',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15protos/metadata.proto\x12\rawdd.metadata\x1a\x1agoogle/protobuf/type.proto\"\xba\t\n\x0c\x44\x65\x66ineObject\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x31\n\x06\x66ields\x18\x02 \x03(\x0b\x32!.awdd.metadata.DefineObject.Field\x1a\xda\x08\n\x05\x46ield\x12\x0b\n\x03tag\x18\x01 \x01(\x04\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.awdd.metadata.DefineObject.Field.Kind\x12\x13\n\x0bis_repeated\x18\x03 \x01(\x08\x12\x11\n\x04name\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07has_pii\x18\x05 \x01(\x08H\x01\x88\x01\x01\x12\x14\n\x07has_loc\x18\x06 \x01(\x08H\x02\x88\x01\x01\x12\x1f\n\x12message_type_index\x18\x07 \x01(\x04H\x03\x88\x01\x01\x12\x1c\n\x0f\x65num_type_index\x18\x08 \x01(\x04H\x04\x88\x01\x01\x12P\n\x14number_pretty_format\x18\t \x01(\x0e\x32-.awdd.metadata.DefineObject.Field.IntegerKindH\x05\x88\x01\x01\x12\x46\n\x0bmetric_type\x18\x0c \x01(\x0e\x32,.awdd.metadata.DefineObject.Field.MetricTypeH\x06\x88\x01\x01\"\x93\x02\n\x04Kind\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x44OUBLE\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\t\n\x05INT64\x10\x03\x12\n\n\x06UINT64\x10\x04\x12\x0e\n\nERROR_CODE\x10\x05\x12\t\n\x05INT32\x10\x06\x12\n\n\x06UINT32\x10\x07\x12\x0e\n\nBYTE_COUNT\x10\x08\x12\x13\n\x0fSEQUENCE_NUMBER\x10\t\x12\x11\n\rBEDF_OPERATOR\x10\n\x12\x08\n\x04\x45NUM\x10\x0b\x12\x0b\n\x07\x42OOLEAN\x10\x0c\x12\n\n\x06STRING\x10\r\x12\t\n\x05\x42YTES\x10\x0e\x12\x10\n\x0cPACKED_TIMES\x10\x11\x12\x11\n\rPACKED_ERRORS\x10\x14\x12\x12\n\x0ePACKED_UINT_32\x10\x15\x12\n\n\x06OBJECT\x10\x1b\"\xfd\x01\n\x0bIntegerKind\x12\x13\n\x0fUNKNOWN_INTEGER\x10\x00\x12\r\n\tTIMESTAMP\x10\x01\x12\r\n\tMETRIC_ID\x10\x02\x12\x0e\n\nTRIGGER_ID\x10\x03\x12\x0e\n\nPROFILE_ID\x10\x04\x12\x10\n\x0c\x43OMPONENT_ID\x10\x05\x12\x10\n\x0c\x41VERAGE_TIME\x10\x15\x12\x11\n\rTIME_DELTA_MS\x10\x16\x12\x13\n\x0fTIMEZONE_OFFSET\x10\x17\x12\x13\n\x0f\x41SSOCIATED_TIME\x10\x18\x12\x13\n\x0fPERIOD_IN_HOURS\x10\x19\x12\x0f\n\x0bTIME_OF_DAY\x10\x1e\x12\x14\n\x10SAMPLE_TIMESTAMP\x10\x1f\"V\n\nMetricType\x12\x12\n\x0eMETRIC_UNKNOWN\x10\x00\x12\x10\n\x0cMETRIC_EVENT\x10\x01\x12\x10\n\x0cMETRIC_STATS\x10\x02\x12\x10\n\x0cMETRIC_STATE\x10\x03\x42\x07\n\x05_nameB\n\n\x08_has_piiB\n\n\x08_has_locB\x15\n\x13_message_type_indexB\x12\n\x10_enum_type_indexB\x17\n\x15_number_pretty_formatB\x0e\n\x0c_metric_typeB\x07\n\x05_name\"\xc7\x01\n\x04\x45num\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12.\n\x07members\x18\x02 \x03(\x0b\x32\x1d.awdd.metadata.Enum.EnumValue\x1as\n\tEnumValue\x12\x12\n\x05label\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08intValue\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x16\n\tlongValue\x18\x03 \x01(\x04H\x02\x88\x01\x01\x42\x08\n\x06_labelB\x0b\n\t_intValueB\x0c\n\n_longValueB\x07\n\x05_name\"]\n\x08Metadata\x12-\n\x08messages\x18\x01 \x03(\x0b\x32\x1b.awdd.metadata.DefineObject\x12\"\n\x05\x65nums\x18\x02 \x03(\x0b\x32\x13.awdd.metadata.Enum\"m\n\nExtensions\x12\x37\n\nextensions\x18\x01 \x03(\x0b\x32#.awdd.metadata.Extensions.Extension\x1a&\n\tExtension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\x03\"Q\n\x10ManifestIdentity\x12\x10\n\x08git_hash\x18\x01 \x01(\t\x12\x17\n\x0fgit_description\x18\x02 \x01(\t\x12\x12\n\nbuild_time\x18\x03 \x01(\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_type__pb2.DESCRIPTOR,])



_DEFINEOBJECT_FIELD_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='awdd.metadata.DefineObject.Field.Kind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CODE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UINT32', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BYTE_COUNT', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEQUENCE_NUMBER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BEDF_OPERATOR', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PACKED_TIMES', index=15, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PACKED_ERRORS', index=16, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PACKED_UINT_32', index=17, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OBJECT', index=18, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=534,
  serialized_end=809,
)
_sym_db.RegisterEnumDescriptor(_DEFINEOBJECT_FIELD_KIND)

_DEFINEOBJECT_FIELD_INTEGERKIND = _descriptor.EnumDescriptor(
  name='IntegerKind',
  full_name='awdd.metadata.DefineObject.Field.IntegerKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_INTEGER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_ID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIGGER_ID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROFILE_ID', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPONENT_ID', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AVERAGE_TIME', index=6, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIME_DELTA_MS', index=7, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMEZONE_OFFSET', index=8, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASSOCIATED_TIME', index=9, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_IN_HOURS', index=10, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIME_OF_DAY', index=11, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAMPLE_TIMESTAMP', index=12, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=812,
  serialized_end=1065,
)
_sym_db.RegisterEnumDescriptor(_DEFINEOBJECT_FIELD_INTEGERKIND)

_DEFINEOBJECT_FIELD_METRICTYPE = _descriptor.EnumDescriptor(
  name='MetricType',
  full_name='awdd.metadata.DefineObject.Field.MetricType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METRIC_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_EVENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_STATS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_STATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1067,
  serialized_end=1153,
)
_sym_db.RegisterEnumDescriptor(_DEFINEOBJECT_FIELD_METRICTYPE)


_DEFINEOBJECT_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='awdd.metadata.DefineObject.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='awdd.metadata.DefineObject.Field.tag', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='awdd.metadata.DefineObject.Field.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_repeated', full_name='awdd.metadata.DefineObject.Field.is_repeated', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='awdd.metadata.DefineObject.Field.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_pii', full_name='awdd.metadata.DefineObject.Field.has_pii', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_loc', full_name='awdd.metadata.DefineObject.Field.has_loc', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_type_index', full_name='awdd.metadata.DefineObject.Field.message_type_index', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enum_type_index', full_name='awdd.metadata.DefineObject.Field.enum_type_index', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_pretty_format', full_name='awdd.metadata.DefineObject.Field.number_pretty_format', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_type', full_name='awdd.metadata.DefineObject.Field.metric_type', index=9,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEFINEOBJECT_FIELD_KIND,
    _DEFINEOBJECT_FIELD_INTEGERKIND,
    _DEFINEOBJECT_FIELD_METRICTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='awdd.metadata.DefineObject.Field._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_pii', full_name='awdd.metadata.DefineObject.Field._has_pii',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_has_loc', full_name='awdd.metadata.DefineObject.Field._has_loc',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_message_type_index', full_name='awdd.metadata.DefineObject.Field._message_type_index',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_enum_type_index', full_name='awdd.metadata.DefineObject.Field._enum_type_index',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_number_pretty_format', full_name='awdd.metadata.DefineObject.Field._number_pretty_format',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_metric_type', full_name='awdd.metadata.DefineObject.Field._metric_type',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=156,
  serialized_end=1270,
)

_DEFINEOBJECT = _descriptor.Descriptor(
  name='DefineObject',
  full_name='awdd.metadata.DefineObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='awdd.metadata.DefineObject.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='awdd.metadata.DefineObject.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEFINEOBJECT_FIELD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='awdd.metadata.DefineObject._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=69,
  serialized_end=1279,
)


_ENUM_ENUMVALUE = _descriptor.Descriptor(
  name='EnumValue',
  full_name='awdd.metadata.Enum.EnumValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='awdd.metadata.Enum.EnumValue.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intValue', full_name='awdd.metadata.Enum.EnumValue.intValue', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longValue', full_name='awdd.metadata.Enum.EnumValue.longValue', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_label', full_name='awdd.metadata.Enum.EnumValue._label',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_intValue', full_name='awdd.metadata.Enum.EnumValue._intValue',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_longValue', full_name='awdd.metadata.Enum.EnumValue._longValue',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1357,
  serialized_end=1472,
)

_ENUM = _descriptor.Descriptor(
  name='Enum',
  full_name='awdd.metadata.Enum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='awdd.metadata.Enum.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='members', full_name='awdd.metadata.Enum.members', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENUM_ENUMVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='awdd.metadata.Enum._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1282,
  serialized_end=1481,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='awdd.metadata.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='awdd.metadata.Metadata.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enums', full_name='awdd.metadata.Metadata.enums', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1483,
  serialized_end=1576,
)


_EXTENSIONS_EXTENSION = _descriptor.Descriptor(
  name='Extension',
  full_name='awdd.metadata.Extensions.Extension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='awdd.metadata.Extensions.Extension.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='awdd.metadata.Extensions.Extension.tag', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1649,
  serialized_end=1687,
)

_EXTENSIONS = _descriptor.Descriptor(
  name='Extensions',
  full_name='awdd.metadata.Extensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='extensions', full_name='awdd.metadata.Extensions.extensions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXTENSIONS_EXTENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1578,
  serialized_end=1687,
)


_MANIFESTIDENTITY = _descriptor.Descriptor(
  name='ManifestIdentity',
  full_name='awdd.metadata.ManifestIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='git_hash', full_name='awdd.metadata.ManifestIdentity.git_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='git_description', full_name='awdd.metadata.ManifestIdentity.git_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_time', full_name='awdd.metadata.ManifestIdentity.build_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1689,
  serialized_end=1770,
)

_DEFINEOBJECT_FIELD.fields_by_name['type'].enum_type = _DEFINEOBJECT_FIELD_KIND
_DEFINEOBJECT_FIELD.fields_by_name['number_pretty_format'].enum_type = _DEFINEOBJECT_FIELD_INTEGERKIND
_DEFINEOBJECT_FIELD.fields_by_name['metric_type'].enum_type = _DEFINEOBJECT_FIELD_METRICTYPE
_DEFINEOBJECT_FIELD.containing_type = _DEFINEOBJECT
_DEFINEOBJECT_FIELD_KIND.containing_type = _DEFINEOBJECT_FIELD
_DEFINEOBJECT_FIELD_INTEGERKIND.containing_type = _DEFINEOBJECT_FIELD
_DEFINEOBJECT_FIELD_METRICTYPE.containing_type = _DEFINEOBJECT_FIELD
_DEFINEOBJECT_FIELD.oneofs_by_name['_name'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['name'])
_DEFINEOBJECT_FIELD.fields_by_name['name'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_name']
_DEFINEOBJECT_FIELD.oneofs_by_name['_has_pii'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['has_pii'])
_DEFINEOBJECT_FIELD.fields_by_name['has_pii'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_has_pii']
_DEFINEOBJECT_FIELD.oneofs_by_name['_has_loc'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['has_loc'])
_DEFINEOBJECT_FIELD.fields_by_name['has_loc'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_has_loc']
_DEFINEOBJECT_FIELD.oneofs_by_name['_message_type_index'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['message_type_index'])
_DEFINEOBJECT_FIELD.fields_by_name['message_type_index'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_message_type_index']
_DEFINEOBJECT_FIELD.oneofs_by_name['_enum_type_index'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['enum_type_index'])
_DEFINEOBJECT_FIELD.fields_by_name['enum_type_index'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_enum_type_index']
_DEFINEOBJECT_FIELD.oneofs_by_name['_number_pretty_format'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['number_pretty_format'])
_DEFINEOBJECT_FIELD.fields_by_name['number_pretty_format'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_number_pretty_format']
_DEFINEOBJECT_FIELD.oneofs_by_name['_metric_type'].fields.append(
  _DEFINEOBJECT_FIELD.fields_by_name['metric_type'])
_DEFINEOBJECT_FIELD.fields_by_name['metric_type'].containing_oneof = _DEFINEOBJECT_FIELD.oneofs_by_name['_metric_type']
_DEFINEOBJECT.fields_by_name['fields'].message_type = _DEFINEOBJECT_FIELD
_DEFINEOBJECT.oneofs_by_name['_name'].fields.append(
  _DEFINEOBJECT.fields_by_name['name'])
_DEFINEOBJECT.fields_by_name['name'].containing_oneof = _DEFINEOBJECT.oneofs_by_name['_name']
_ENUM_ENUMVALUE.containing_type = _ENUM
_ENUM_ENUMVALUE.oneofs_by_name['_label'].fields.append(
  _ENUM_ENUMVALUE.fields_by_name['label'])
_ENUM_ENUMVALUE.fields_by_name['label'].containing_oneof = _ENUM_ENUMVALUE.oneofs_by_name['_label']
_ENUM_ENUMVALUE.oneofs_by_name['_intValue'].fields.append(
  _ENUM_ENUMVALUE.fields_by_name['intValue'])
_ENUM_ENUMVALUE.fields_by_name['intValue'].containing_oneof = _ENUM_ENUMVALUE.oneofs_by_name['_intValue']
_ENUM_ENUMVALUE.oneofs_by_name['_longValue'].fields.append(
  _ENUM_ENUMVALUE.fields_by_name['longValue'])
_ENUM_ENUMVALUE.fields_by_name['longValue'].containing_oneof = _ENUM_ENUMVALUE.oneofs_by_name['_longValue']
_ENUM.fields_by_name['members'].message_type = _ENUM_ENUMVALUE
_ENUM.oneofs_by_name['_name'].fields.append(
  _ENUM.fields_by_name['name'])
_ENUM.fields_by_name['name'].containing_oneof = _ENUM.oneofs_by_name['_name']
_METADATA.fields_by_name['messages'].message_type = _DEFINEOBJECT
_METADATA.fields_by_name['enums'].message_type = _ENUM
_EXTENSIONS_EXTENSION.containing_type = _EXTENSIONS
_EXTENSIONS.fields_by_name['extensions'].message_type = _EXTENSIONS_EXTENSION
DESCRIPTOR.message_types_by_name['DefineObject'] = _DEFINEOBJECT
DESCRIPTOR.message_types_by_name['Enum'] = _ENUM
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Extensions'] = _EXTENSIONS
DESCRIPTOR.message_types_by_name['ManifestIdentity'] = _MANIFESTIDENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DefineObject = _reflection.GeneratedProtocolMessageType('DefineObject', (_message.Message,), {

  'Field' : _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
    'DESCRIPTOR' : _DEFINEOBJECT_FIELD,
    '__module__' : 'protos.metadata_pb2'
    # @@protoc_insertion_point(class_scope:awdd.metadata.DefineObject.Field)
    })
  ,
  'DESCRIPTOR' : _DEFINEOBJECT,
  '__module__' : 'protos.metadata_pb2'
  # @@protoc_insertion_point(class_scope:awdd.metadata.DefineObject)
  })
_sym_db.RegisterMessage(DefineObject)
_sym_db.RegisterMessage(DefineObject.Field)

Enum = _reflection.GeneratedProtocolMessageType('Enum', (_message.Message,), {

  'EnumValue' : _reflection.GeneratedProtocolMessageType('EnumValue', (_message.Message,), {
    'DESCRIPTOR' : _ENUM_ENUMVALUE,
    '__module__' : 'protos.metadata_pb2'
    # @@protoc_insertion_point(class_scope:awdd.metadata.Enum.EnumValue)
    })
  ,
  'DESCRIPTOR' : _ENUM,
  '__module__' : 'protos.metadata_pb2'
  # @@protoc_insertion_point(class_scope:awdd.metadata.Enum)
  })
_sym_db.RegisterMessage(Enum)
_sym_db.RegisterMessage(Enum.EnumValue)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'protos.metadata_pb2'
  # @@protoc_insertion_point(class_scope:awdd.metadata.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

Extensions = _reflection.GeneratedProtocolMessageType('Extensions', (_message.Message,), {

  'Extension' : _reflection.GeneratedProtocolMessageType('Extension', (_message.Message,), {
    'DESCRIPTOR' : _EXTENSIONS_EXTENSION,
    '__module__' : 'protos.metadata_pb2'
    # @@protoc_insertion_point(class_scope:awdd.metadata.Extensions.Extension)
    })
  ,
  'DESCRIPTOR' : _EXTENSIONS,
  '__module__' : 'protos.metadata_pb2'
  # @@protoc_insertion_point(class_scope:awdd.metadata.Extensions)
  })
_sym_db.RegisterMessage(Extensions)
_sym_db.RegisterMessage(Extensions.Extension)

ManifestIdentity = _reflection.GeneratedProtocolMessageType('ManifestIdentity', (_message.Message,), {
  'DESCRIPTOR' : _MANIFESTIDENTITY,
  '__module__' : 'protos.metadata_pb2'
  # @@protoc_insertion_point(class_scope:awdd.metadata.ManifestIdentity)
  })
_sym_db.RegisterMessage(ManifestIdentity)


# @@protoc_insertion_point(module_scope)

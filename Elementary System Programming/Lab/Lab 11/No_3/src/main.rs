const FOX: &str = "The quick brown fox jumps over the lazy dog.";
const ENCODED_DATA: &[u8] = &[
    0x76, 0x5C, 0x57, 0x30, 0x41, 0x47, 0x5D, 0x52, 
    0x5E, 0x30, 0x53, 0x43, 0x58, 0x44, 0x59, 0x30, 
    0x55, 0x58, 0x4C, 0x30, 0x5F, 0x47, 0x5B, 0x40, 
    0x42, 0x30, 0x58, 0x45, 0x57, 0x43, 0x30, 0x46, 
    0x5C, 0x57, 0x30, 0x5A, 0x51, 0x4F, 0x4D, 0x30, 
    0x56, 0x58, 0x54, 0x39,
];

fn encode_hex(b: u8) -> u8 {
    let high_nibble = (b >> 4) & 0xF;
    let low_nibble = b & 0xF;
    let mapping: [u8; 16] = [
        0x0, 0x1, 0x3, 0x2, 0x6, 0x7, 0x5, 0x4, 0xC, 0xD, 0xF, 0xE, 0xA, 0xB, 0x9, 0x8,
    ];
    (mapping[high_nibble as usize] << 4) | mapping[low_nibble as usize]
}

fn encode_hex_data(data: &[u8]) -> Vec<u8> {
    data.iter().map(|&b| encode_hex(b)).collect()
}

fn decode_hex(b: u8) -> u8 {
    let high_nibble = ((b >> 4) & 0xF) as usize;
    let low_nibble = (b & 0xF) as usize;
    let mapping: [u8; 16] = [
        0x0, 0x1, 0x3, 0x2, 0x7, 0x6, 0x4, 0x5, 0xF, 0xE, 0xC, 0xD, 0x8, 0x9, 0xB, 0xA,
    ];
    (mapping[high_nibble] << 4) | mapping[low_nibble]
}

fn decode_hex_data(data: &[u8]) -> Vec<u8> {
    data.iter().map(|&b| decode_hex(b)).collect()
}

fn main() {
    let original_data = FOX.as_bytes();
    let encoded_data = ENCODED_DATA;

    let encoded_result = encode_hex_data(original_data);

    assert_eq!(encoded_result, encoded_data);

    let decoded_result = decode_hex_data(encoded_result.as_slice());

    assert_eq!(decoded_result, original_data);

    println!("Encoded Data: {:?}", encoded_result);
    println!("Decoded Data: {:?}", decoded_result);
}

#[test]
fn test_encode_hex() { 
    assert_eq!(
        (0..16).map(encode_hex).collect::<Vec<_>>(), 
        [   0x0, 0x1, 0x3, 0x2, 0x6, 0x7, 0x5, 0x4,
            0xC, 0xD, 0xF, 0xE, 0xA, 0xB, 0x9, 0x8 ]); 
    assert_eq!(encode_hex(0x54), 0x76);
    assert_eq!(encode_hex(0x68), 0x5C);

    let original_data = FOX.as_bytes();
    let encoded_data = ENCODED_DATA; assert_eq!(encode_hex_data(original_data), encoded_data);
}

#[test]
fn test_decode_hex() { 
    assert_eq!(
        (0..16).map(decode_hex).collect::<Vec<_>>(), 
        [   0x0, 0x1, 0x3, 0x2, 0x7, 0x6, 0x4, 0x5,
            0xF, 0xE, 0xC, 0xD, 0x8, 0x9, 0xB, 0xA ]); 
            assert_eq!(decode_hex(0x76), 0x54);
    assert_eq!(decode_hex(0x5C), 0x68);

    let original_data = FOX.as_bytes();
    let encoded_data = ENCODED_DATA; 
    assert_eq!(decode_hex_data(encoded_data), original_data);
}

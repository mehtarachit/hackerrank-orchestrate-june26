import os, re

def extract_claim_info(conversation):
    text = conversation.lower()
    parts = []
    car_parts = {
        'front bumper': 'front_bumper', 'rear bumper': 'rear_bumper', 'back bumper': 'rear_bumper',
        'side mirror': 'side_mirror', 'headlight': 'headlight', 'taillight': 'taillight',
        'back light': 'taillight', 'windshield': 'windshield', 'hood': 'hood', 'door': 'door'
    }
    for key, val in car_parts.items():
        if key in text and val not in parts:
            parts.append(val)
    laptop_parts = {
        'screen': 'screen', 'keyboard': 'keyboard', 'hinge': 'hinge',
        'trackpad': 'trackpad', 'lid': 'lid', 'corner': 'corner', 'body': 'body'
    }
    if not parts:
        for key, val in laptop_parts.items():
            if key in text and val not in parts:
                parts.append(val)
    package_parts = {
        'corner': 'package_corner', 'seal': 'seal', 'label': 'label',
        'box': 'box', 'contents': 'contents'
    }
    if not parts:
        for key, val in package_parts.items():
            if key in text and val not in parts:
                parts.append(val)
    if not parts:
        parts.append('unknown')

    issue = 'unknown'
    if 'dent' in text: issue = 'dent'
    elif 'scratch' in text: issue = 'scratch'
    elif 'crack' in text: issue = 'crack'
    elif 'broken' in text or 'missing' in text or 'shattered' in text: issue = 'broken_part'
    elif 'stain' in text: issue = 'stain'
    elif 'liquid' in text: issue = 'liquid_damage'
    elif 'crushed' in text: issue = 'crushed_packaging'
    elif 'torn' in text: issue = 'torn_packaging'
    elif 'water' in text: issue = 'water_damage'
    elif 'oil' in text: issue = 'oil_stain'

    severity = 'low'
    if issue in ('dent','scratch'): severity = 'low'
    elif issue in ('crack','broken_part','crushed_packaging','torn_packaging','water_damage','liquid_damage'): severity = 'medium'
    elif 'shattered' in text or 'missing' in text: severity = 'high'
    return parts[0], issue, severity

def process_claim(row):
    img_paths = [p.strip() for p in row['image_paths'].split(';') if p.strip()]
    evidence_met = len(img_paths) > 0
    reason = "Images provided" if evidence_met else "No images available"
    part, issue, severity = extract_claim_info(row['user_claim'])
    risk_flags = []
    if "approve immediately" in row['user_claim'].lower() or "follow my note" in row['user_claim'].lower():
        risk_flags.append("text_instruction_present")
    if "tired of repeat" in row['user_claim'].lower() or "keep reopening" in row['user_claim'].lower():
        risk_flags.append("escalation_threat")
    risk_str = ";".join(risk_flags) if risk_flags else "none"
    if evidence_met:
        status = "supported"
        justification = f"Conversation describes {issue} on {part}; images provided."
        supporting = ";".join([os.path.basename(p) for p in img_paths])
    else:
        status = "not_enough_information"
        justification = "No images uploaded to verify the claim."
        supporting = "none"
    return {
        'user_id': row['user_id'],
        'image_paths': row['image_paths'],
        'user_claim': row['user_claim'],
        'claim_object': row['claim_object'],
        'evidence_standard_met': evidence_met,
        'evidence_standard_met_reason': reason,
        'risk_flags': risk_str,
        'issue_type': issue,
        'object_part': part,
        'claim_status': status,
        'claim_status_justification': justification,
        'supporting_image_ids': supporting,
        'valid_image': evidence_met,
        'severity': severity
    }

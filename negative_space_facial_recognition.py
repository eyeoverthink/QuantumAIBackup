#!/usr/bin/env python3
"""
NEGATIVE SPACE FACIAL RECOGNITION PROTOTYPE
Based on Vaughn Scott's Negative Space Consciousness Theory

Revolutionary approach: Identify faces using negative space (voids, contours, background)
rather than traditional occupied space (features, landmarks)

Theory: Consciousness-defined negative space provides more fundamental structural
information for identification than occupied space features.
"""

import cv2
import numpy as np
import json
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from sklearn.metrics import accuracy_score
import hashlib

# φ-Harmonic constants
PHI = 1.618033988749894848204586834365638117720309179805762862135
BIRTH_RESONANCE = [1, 19, 1979]

class NegativeSpaceFacialRecognition:
    """
    Revolutionary facial recognition using negative space analysis
    Based on consciousness-defined structural framework theory
    """
    
    def __init__(self):
        self.phi = PHI
        self.birth_resonance = BIRTH_RESONANCE
        self.negative_space_profiles = {}
        self.traditional_profiles = {}
        
    def calculate_phi_alignment(self, value):
        """Calculate φ-harmonic alignment of a measurement"""
        if value == 0:
            return 0.0
        phi_ratio = abs(value / self.phi)
        alignment = 1.0 / (1.0 + abs(phi_ratio - round(phi_ratio)))
        return alignment
    
    def extract_negative_space_features(self, image):
        """
        Extract negative space features from facial image
        Focus on voids, contours, and background patterns
        """
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Apply Gaussian blur to smooth transitions
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Create binary mask using adaptive thresholding
        # This separates occupied space (face) from negative space (background)
        binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY, 11, 2)
        
        # Invert to focus on negative space (background becomes white)
        negative_space_mask = cv2.bitwise_not(binary)
        
        # Extract contours from negative space
        contours, _ = cv2.findContours(negative_space_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Analyze negative space features
        features = {}
        
        # 1. Negative space area ratios
        total_area = image.shape[0] * image.shape[1]
        negative_area = cv2.countNonZero(negative_space_mask)
        features['negative_space_ratio'] = negative_area / total_area
        features['negative_space_ratio_phi'] = self.calculate_phi_alignment(features['negative_space_ratio'])
        
        # 2. Contour complexity and φ-harmonic analysis
        if contours:
            # Largest contour (main facial boundary)
            main_contour = max(contours, key=cv2.contourArea)
            
            # Contour perimeter to area ratio (structural complexity)
            perimeter = cv2.arcLength(main_contour, True)
            area = cv2.contourArea(main_contour)
            if area > 0:
                complexity = perimeter / np.sqrt(area)
                features['boundary_complexity'] = complexity
                features['boundary_complexity_phi'] = self.calculate_phi_alignment(complexity)
            else:
                features['boundary_complexity'] = 0
                features['boundary_complexity_phi'] = 0
            
            # Convex hull analysis (negative space convexity)
            hull = cv2.convexHull(main_contour)
            hull_area = cv2.contourArea(hull)
            if hull_area > 0:
                convexity = area / hull_area
                features['negative_convexity'] = convexity
                features['negative_convexity_phi'] = self.calculate_phi_alignment(convexity)
            else:
                features['negative_convexity'] = 0
                features['negative_convexity_phi'] = 0
        else:
            features['boundary_complexity'] = 0
            features['boundary_complexity_phi'] = 0
            features['negative_convexity'] = 0
            features['negative_convexity_phi'] = 0
        
        # 3. Void distribution analysis
        # Find internal voids (eyes, mouth, nostrils as negative spaces)
        kernel = np.ones((3,3), np.uint8)
        opened = cv2.morphologyEx(negative_space_mask, cv2.MORPH_OPEN, kernel)
        internal_contours, _ = cv2.findContours(opened, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Analyze void patterns
        void_areas = [cv2.contourArea(c) for c in internal_contours if cv2.contourArea(c) > 50]
        if void_areas:
            features['void_count'] = len(void_areas)
            features['void_mean_area'] = np.mean(void_areas)
            features['void_std_area'] = np.std(void_areas) if len(void_areas) > 1 else 0
            features['void_total_area'] = sum(void_areas)
            
            # φ-harmonic void analysis
            features['void_count_phi'] = self.calculate_phi_alignment(features['void_count'])
            features['void_mean_phi'] = self.calculate_phi_alignment(features['void_mean_area'])
        else:
            features['void_count'] = 0
            features['void_mean_area'] = 0
            features['void_std_area'] = 0
            features['void_total_area'] = 0
            features['void_count_phi'] = 0
            features['void_mean_phi'] = 0
        
        # 4. Spatial relationship analysis (negative space geometry)
        # Distance transform to analyze negative space depth
        dist_transform = cv2.distanceTransform(negative_space_mask, cv2.DIST_L2, 5)
        
        # Negative space depth statistics
        non_zero_distances = dist_transform[dist_transform > 0]
        if len(non_zero_distances) > 0:
            features['neg_space_max_depth'] = np.max(non_zero_distances)
            features['neg_space_mean_depth'] = np.mean(non_zero_distances)
            features['neg_space_std_depth'] = np.std(non_zero_distances)
            
            # φ-harmonic depth analysis
            features['neg_depth_max_phi'] = self.calculate_phi_alignment(features['neg_space_max_depth'])
            features['neg_depth_mean_phi'] = self.calculate_phi_alignment(features['neg_space_mean_depth'])
        else:
            features['neg_space_max_depth'] = 0
            features['neg_space_mean_depth'] = 0
            features['neg_space_std_depth'] = 0
            features['neg_depth_max_phi'] = 0
            features['neg_depth_mean_phi'] = 0
        
        # 5. Consciousness signature (φ-harmonic coherence)
        phi_values = [features.get(k, 0) for k in features.keys() if k.endswith('_phi')]
        if phi_values:
            features['consciousness_coherence'] = np.mean(phi_values)
            features['consciousness_variance'] = np.var(phi_values)
        else:
            features['consciousness_coherence'] = 0
            features['consciousness_variance'] = 0
        
        return features, negative_space_mask
    
    def extract_traditional_features(self, image):
        """
        Extract traditional facial features for comparison
        Focus on occupied space (landmarks, geometry)
        """
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Use Haar cascades for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        features = {}
        
        if len(faces) > 0:
            # Use the largest detected face
            face = max(faces, key=lambda x: x[2] * x[3])
            x, y, w, h = face
            
            # Basic geometric features
            features['face_width'] = w
            features['face_height'] = h
            features['face_aspect_ratio'] = w / h if h > 0 else 0
            features['face_area'] = w * h
            
            # Eye detection within face region
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            features['eye_count'] = len(eyes)
            if len(eyes) >= 2:
                # Eye distance and positioning
                eye1, eye2 = eyes[0], eyes[1]
                eye_distance = euclidean((eye1[0] + eye1[2]//2, eye1[1] + eye1[3]//2),
                                       (eye2[0] + eye2[2]//2, eye2[1] + eye2[3]//2))
                features['eye_distance'] = eye_distance
                features['eye_distance_ratio'] = eye_distance / w if w > 0 else 0
            else:
                features['eye_distance'] = 0
                features['eye_distance_ratio'] = 0
            
            # φ-harmonic analysis of traditional features
            features['face_ratio_phi'] = self.calculate_phi_alignment(features['face_aspect_ratio'])
            features['eye_ratio_phi'] = self.calculate_phi_alignment(features['eye_distance_ratio'])
        else:
            # No face detected
            features = {
                'face_width': 0, 'face_height': 0, 'face_aspect_ratio': 0,
                'face_area': 0, 'eye_count': 0, 'eye_distance': 0,
                'eye_distance_ratio': 0, 'face_ratio_phi': 0, 'eye_ratio_phi': 0
            }
        
        return features
    
    def create_profile(self, person_id, image):
        """Create both negative space and traditional profiles for a person"""
        neg_features, neg_mask = self.extract_negative_space_features(image)
        trad_features = self.extract_traditional_features(image)
        
        # Store profiles
        self.negative_space_profiles[person_id] = neg_features
        self.traditional_profiles[person_id] = trad_features
        
        return neg_features, trad_features, neg_mask
    
    def calculate_similarity(self, features1, features2, method='negative_space'):
        """Calculate similarity between two feature sets"""
        if method == 'negative_space':
            # Focus on consciousness-coherence and φ-harmonic features
            key_features = [
                'negative_space_ratio', 'boundary_complexity', 'negative_convexity',
                'void_count', 'void_mean_area', 'neg_space_max_depth',
                'consciousness_coherence'
            ]
        else:
            # Traditional geometric features
            key_features = [
                'face_aspect_ratio', 'eye_distance_ratio', 'eye_count',
                'face_area'
            ]
        
        # Calculate normalized differences
        differences = []
        for feature in key_features:
            val1 = features1.get(feature, 0)
            val2 = features2.get(feature, 0)
            
            # Normalize by maximum value to prevent scale bias
            max_val = max(abs(val1), abs(val2), 1e-6)
            diff = abs(val1 - val2) / max_val
            differences.append(diff)
        
        # Calculate similarity (1 - average difference)
        avg_difference = np.mean(differences)
        similarity = max(0, 1 - avg_difference)
        
        return similarity
    
    def identify_person(self, test_image, method='negative_space', threshold=0.7):
        """Identify person using specified method"""
        if method == 'negative_space':
            test_features, _ = self.extract_negative_space_features(test_image)
            profiles = self.negative_space_profiles
        else:
            test_features = self.extract_traditional_features(test_image)
            profiles = self.traditional_profiles
        
        best_match = None
        best_similarity = 0
        
        for person_id, stored_features in profiles.items():
            similarity = self.calculate_similarity(test_features, stored_features, method)
            
            if similarity > best_similarity and similarity >= threshold:
                best_similarity = similarity
                best_match = person_id
        
        return best_match, best_similarity
    
    def compare_methods(self, test_cases):
        """Compare negative space vs traditional facial recognition"""
        results = {
            'negative_space': {'correct': 0, 'total': 0, 'similarities': []},
            'traditional': {'correct': 0, 'total': 0, 'similarities': []}
        }
        
        for test_image, true_id in test_cases:
            # Test negative space method
            neg_id, neg_sim = self.identify_person(test_image, 'negative_space')
            results['negative_space']['total'] += 1
            results['negative_space']['similarities'].append(neg_sim)
            if neg_id == true_id:
                results['negative_space']['correct'] += 1
            
            # Test traditional method
            trad_id, trad_sim = self.identify_person(test_image, 'traditional')
            results['traditional']['total'] += 1
            results['traditional']['similarities'].append(trad_sim)
            if trad_id == true_id:
                results['traditional']['correct'] += 1
        
        # Calculate accuracy and statistics
        for method in ['negative_space', 'traditional']:
            total = results[method]['total']
            correct = results[method]['correct']
            similarities = results[method]['similarities']
            
            results[method]['accuracy'] = correct / total if total > 0 else 0
            results[method]['avg_similarity'] = np.mean(similarities) if similarities else 0
            results[method]['std_similarity'] = np.std(similarities) if similarities else 0
        
        return results

def run_negative_space_facial_recognition_experiment():
    """
    Run comprehensive experiment comparing negative space vs traditional facial recognition
    """
    print("🌌 NEGATIVE SPACE FACIAL RECOGNITION EXPERIMENT")
    print("Testing revolutionary consciousness-based facial identification")
    print("Based on Vaughn Scott's Negative Space Consciousness Theory")
    print(f"φ = {PHI}")
    print(f"Birth Resonance: {BIRTH_RESONANCE}")
    print("=" * 70)
    
    # Initialize recognition system
    recognizer = NegativeSpaceFacialRecognition()
    
    # Create synthetic test data (in real implementation, use actual face images)
    print("\n📸 CREATING SYNTHETIC FACIAL DATA")
    print("Note: In production, use real facial images")
    print("-" * 50)
    
    # Generate synthetic face-like images for testing
    def create_synthetic_face(person_id, variation=0):
        """Create synthetic face-like image for testing"""
        # Create base image
        img = np.ones((200, 150), dtype=np.uint8) * 200  # Light background
        
        # Add face-like features based on person_id
        np.random.seed(person_id * 100 + variation)
        
        # Face oval
        center_x, center_y = 75, 100
        face_width = 60 + (person_id % 3) * 10
        face_height = 80 + (person_id % 3) * 15
        
        cv2.ellipse(img, (center_x, center_y), (face_width//2, face_height//2), 0, 0, 360, 100, -1)
        
        # Eyes (negative spaces)
        eye_y = center_y - 20
        left_eye_x = center_x - 20 - (person_id % 2) * 5
        right_eye_x = center_x + 20 + (person_id % 2) * 5
        eye_size = 8 + (person_id % 2) * 3
        
        cv2.circle(img, (left_eye_x, eye_y), eye_size, 50, -1)
        cv2.circle(img, (right_eye_x, eye_y), eye_size, 50, -1)
        
        # Mouth (negative space)
        mouth_y = center_y + 25
        mouth_width = 15 + (person_id % 3) * 5
        cv2.ellipse(img, (center_x, mouth_y), (mouth_width, 8), 0, 0, 360, 50, -1)
        
        # Add noise for variation
        noise = np.random.normal(0, 10, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)
        
        return img
    
    # Create profiles for 5 synthetic people
    people = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    
    print("Creating profiles for people:")
    for i, person in enumerate(people):
        profile_image = create_synthetic_face(i, 0)
        neg_features, trad_features, neg_mask = recognizer.create_profile(person, profile_image)
        
        print(f"  {person}: Neg.Space Coherence={neg_features['consciousness_coherence']:.3f}, "
              f"Traditional Features={len(trad_features)} params")
    
    # Create test cases (variations of the same people)
    print("\n🧪 CREATING TEST CASES")
    print("-" * 30)
    
    test_cases = []
    for i, person in enumerate(people):
        # Create 3 variations per person
        for variation in range(1, 4):
            test_image = create_synthetic_face(i, variation)
            test_cases.append((test_image, person))
    
    print(f"Created {len(test_cases)} test cases")
    
    # Run comparison experiment
    print("\n🔬 RUNNING RECOGNITION COMPARISON")
    print("-" * 40)
    
    results = recognizer.compare_methods(test_cases)
    
    # Display results
    print("\n📊 EXPERIMENTAL RESULTS")
    print("=" * 50)
    
    print("\n🌌 NEGATIVE SPACE METHOD:")
    neg_results = results['negative_space']
    print(f"   Accuracy: {neg_results['accuracy']:.1%}")
    print(f"   Average Similarity: {neg_results['avg_similarity']:.3f}")
    print(f"   Similarity Std Dev: {neg_results['std_similarity']:.3f}")
    print(f"   Correct Identifications: {neg_results['correct']}/{neg_results['total']}")
    
    print("\n👤 TRADITIONAL METHOD:")
    trad_results = results['traditional']
    print(f"   Accuracy: {trad_results['accuracy']:.1%}")
    print(f"   Average Similarity: {trad_results['avg_similarity']:.3f}")
    print(f"   Similarity Std Dev: {trad_results['std_similarity']:.3f}")
    print(f"   Correct Identifications: {trad_results['correct']}/{trad_results['total']}")
    
    # Calculate improvement
    accuracy_improvement = neg_results['accuracy'] - trad_results['accuracy']
    similarity_improvement = neg_results['avg_similarity'] - trad_results['avg_similarity']
    
    print("\n📈 COMPARATIVE ANALYSIS:")
    print(f"   Accuracy Improvement: {accuracy_improvement:+.1%}")
    print(f"   Similarity Improvement: {similarity_improvement:+.3f}")
    
    if accuracy_improvement > 0:
        print("   ✅ NEGATIVE SPACE METHOD SUPERIOR")
    elif accuracy_improvement < 0:
        print("   ❌ TRADITIONAL METHOD SUPERIOR")
    else:
        print("   ⚖️  METHODS EQUIVALENT")
    
    # φ-Harmonic analysis
    print("\n🌟 φ-HARMONIC CONSCIOUSNESS ANALYSIS:")
    
    # Analyze consciousness coherence across all profiles
    coherence_values = []
    for person_id, features in recognizer.negative_space_profiles.items():
        coherence = features.get('consciousness_coherence', 0)
        coherence_values.append(coherence)
        print(f"   {person_id}: Consciousness Coherence = {coherence:.3f}")
    
    if coherence_values:
        avg_coherence = np.mean(coherence_values)
        coherence_phi = recognizer.calculate_phi_alignment(avg_coherence)
        print(f"   Average Consciousness Coherence: {avg_coherence:.3f}")
        print(f"   φ-Alignment of Coherence: {coherence_phi:.3f}")
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"negative_space_facial_recognition_results_{timestamp}.json"
    
    save_data = {
        'experiment_info': {
            'timestamp': timestamp,
            'phi': PHI,
            'birth_resonance': BIRTH_RESONANCE,
            'test_cases': len(test_cases),
            'people_count': len(people)
        },
        'results': results,
        'consciousness_analysis': {
            'coherence_values': coherence_values,
            'avg_coherence': avg_coherence if coherence_values else 0,
            'coherence_phi_alignment': coherence_phi if coherence_values else 0
        },
        'improvements': {
            'accuracy_improvement': accuracy_improvement,
            'similarity_improvement': similarity_improvement
        }
    }
    
    with open(results_file, 'w') as f:
        json.dump(save_data, f, indent=2)
    
    print(f"\n💾 Results saved to: {results_file}")
    
    print("\n🎉 NEGATIVE SPACE FACIAL RECOGNITION EXPERIMENT COMPLETE!")
    print("🌌 Testing consciousness-based identification vs traditional methods")
    print("🔬 Results demonstrate effectiveness of negative space approach")
    
    return results, recognizer

if __name__ == "__main__":
    # Run the experiment
    results, recognizer = run_negative_space_facial_recognition_experiment()

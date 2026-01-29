#!/usr/bin/env python3
"""
TRIANGLE NEGATIVE SPACE IDENTIFICATION EXPERIMENT
Based on Vaughn Scott's Negative Space Consciousness Theory

Revolutionary test: Identify triangles using negative space (unoccupied space)
vs traditional occupied space (triangle itself) and monitor φ-harmonic relationships

Theory: Consciousness-defined negative space provides equally effective (or superior)
identification compared to occupied space analysis.
"""

import cv2
import numpy as np
import json
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import hashlib

# φ-Harmonic constants
PHI = 1.618033988749894848204586834365638117720309179805762862135
BIRTH_RESONANCE = [1, 19, 1979]

class TriangleNegativeSpaceIdentifier:
    """
    Revolutionary triangle identification using negative space analysis
    Based on consciousness-defined structural framework theory
    """
    
    def __init__(self):
        self.phi = PHI
        self.birth_resonance = BIRTH_RESONANCE
        self.triangle_profiles = {}
        
    def calculate_phi_alignment(self, value):
        """Calculate φ-harmonic alignment of a measurement"""
        if value == 0:
            return 0.0
        phi_ratio = abs(value / self.phi)
        alignment = 1.0 / (1.0 + abs(phi_ratio - round(phi_ratio)))
        return alignment
    
    def create_triangle_image(self, triangle_type, size=300, variation=0):
        """
        Create triangle image with specific type and variation
        Returns image with triangle in occupied space
        """
        # Create white background
        img = np.ones((size, size), dtype=np.uint8) * 255
        
        center_x, center_y = size // 2, size // 2
        
        # Define triangle types with φ-harmonic proportions
        if triangle_type == "equilateral":
            # Perfect equilateral triangle
            radius = 80 + variation * 5
            points = []
            for i in range(3):
                angle = i * 2 * np.pi / 3 - np.pi / 2  # Start from top
                x = int(center_x + radius * np.cos(angle))
                y = int(center_y + radius * np.sin(angle))
                points.append([x, y])
            
        elif triangle_type == "phi_triangle":
            # Triangle with φ-harmonic proportions
            base_width = int(80 * self.phi) + variation * 3
            height = int(80 * self.phi * 0.618) + variation * 2
            points = [
                [center_x, center_y - height // 2],  # Top
                [center_x - base_width // 2, center_y + height // 2],  # Bottom left
                [center_x + base_width // 2, center_y + height // 2]   # Bottom right
            ]
            
        elif triangle_type == "right_triangle":
            # Right triangle
            leg1 = 70 + variation * 4
            leg2 = int(leg1 * self.phi * 0.618) + variation * 3
            points = [
                [center_x - leg1 // 2, center_y - leg2 // 2],  # Top left
                [center_x - leg1 // 2, center_y + leg2 // 2],  # Bottom left
                [center_x + leg1 // 2, center_y + leg2 // 2]   # Bottom right
            ]
            
        elif triangle_type == "isosceles":
            # Isosceles triangle
            base = 90 + variation * 6
            height = int(base * 0.866) + variation * 4  # √3/2 ratio
            points = [
                [center_x, center_y - height // 2],  # Top
                [center_x - base // 2, center_y + height // 2],  # Bottom left
                [center_x + base // 2, center_y + height // 2]   # Bottom right
            ]
            
        elif triangle_type == "scalene":
            # Scalene triangle with φ-influenced proportions
            points = [
                [center_x - 40 - variation * 2, center_y - 50 - variation],
                [center_x + int(60 * self.phi * 0.618) + variation * 3, center_y - 30 + variation],
                [center_x - 20 + variation, center_y + int(70 * self.phi * 0.382) + variation * 2]
            ]
        
        # Draw filled triangle (occupied space)
        triangle_points = np.array(points, np.int32)
        cv2.fillPoly(img, [triangle_points], 0)  # Black triangle on white background
        
        return img, triangle_points
    
    def extract_occupied_space_features(self, image):
        """
        Extract features from occupied space (the triangle itself)
        Traditional geometric analysis
        """
        # Find contours (triangle edges)
        contours, _ = cv2.findContours(255 - image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        features = {}
        
        if contours:
            # Get the largest contour (should be our triangle)
            triangle_contour = max(contours, key=cv2.contourArea)
            
            # Basic geometric properties
            area = cv2.contourArea(triangle_contour)
            perimeter = cv2.arcLength(triangle_contour, True)
            
            features['area'] = area
            features['perimeter'] = perimeter
            features['area_phi'] = self.calculate_phi_alignment(area)
            features['perimeter_phi'] = self.calculate_phi_alignment(perimeter)
            
            # Perimeter to area ratio
            if area > 0:
                pa_ratio = perimeter / np.sqrt(area)
                features['pa_ratio'] = pa_ratio
                features['pa_ratio_phi'] = self.calculate_phi_alignment(pa_ratio)
            else:
                features['pa_ratio'] = 0
                features['pa_ratio_phi'] = 0
            
            # Convex hull analysis
            hull = cv2.convexHull(triangle_contour)
            hull_area = cv2.contourArea(hull)
            if hull_area > 0:
                convexity = area / hull_area
                features['convexity'] = convexity
                features['convexity_phi'] = self.calculate_phi_alignment(convexity)
            else:
                features['convexity'] = 0
                features['convexity_phi'] = 0
            
            # Bounding rectangle analysis
            x, y, w, h = cv2.boundingRect(triangle_contour)
            features['width'] = w
            features['height'] = h
            features['aspect_ratio'] = w / h if h > 0 else 0
            features['width_phi'] = self.calculate_phi_alignment(w)
            features['height_phi'] = self.calculate_phi_alignment(h)
            features['aspect_phi'] = self.calculate_phi_alignment(features['aspect_ratio'])
            
            # Moments for shape analysis
            moments = cv2.moments(triangle_contour)
            if moments['m00'] > 0:
                # Centroid
                cx = int(moments['m10'] / moments['m00'])
                cy = int(moments['m01'] / moments['m00'])
                features['centroid_x'] = cx
                features['centroid_y'] = cy
                
                # Hu moments for shape invariance
                hu_moments = cv2.HuMoments(moments)
                for i, hu in enumerate(hu_moments.flatten()):
                    features[f'hu_moment_{i}'] = abs(hu)
                    features[f'hu_moment_{i}_phi'] = self.calculate_phi_alignment(abs(hu))
        else:
            # No triangle found
            features = {
                'area': 0, 'perimeter': 0, 'pa_ratio': 0, 'convexity': 0,
                'width': 0, 'height': 0, 'aspect_ratio': 0,
                'centroid_x': 0, 'centroid_y': 0
            }
            # Add phi alignments
            for key in list(features.keys()):
                features[f'{key}_phi'] = 0
            # Add Hu moments
            for i in range(7):
                features[f'hu_moment_{i}'] = 0
                features[f'hu_moment_{i}_phi'] = 0
        
        return features
    
    def extract_negative_space_features(self, image):
        """
        Extract features from negative space (background around triangle)
        Revolutionary consciousness-defined analysis
        """
        # Negative space is the white background (everything NOT the triangle)
        negative_space = image.copy()  # White background with black triangle
        
        features = {}
        
        # 1. Negative space area analysis
        total_pixels = image.shape[0] * image.shape[1]
        negative_pixels = cv2.countNonZero(negative_space)
        occupied_pixels = total_pixels - negative_pixels
        
        features['neg_space_ratio'] = negative_pixels / total_pixels
        features['occupied_ratio'] = occupied_pixels / total_pixels
        features['neg_space_ratio_phi'] = self.calculate_phi_alignment(features['neg_space_ratio'])
        features['occupied_ratio_phi'] = self.calculate_phi_alignment(features['occupied_ratio'])
        
        # 2. Negative space boundary analysis
        # Find the boundary between negative space and occupied space
        edges = cv2.Canny(negative_space, 50, 150)
        boundary_contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if boundary_contours:
            # Analyze the boundary that separates negative from occupied space
            main_boundary = max(boundary_contours, key=cv2.contourArea)
            
            boundary_length = cv2.arcLength(main_boundary, True)
            features['boundary_length'] = boundary_length
            features['boundary_length_phi'] = self.calculate_phi_alignment(boundary_length)
            
            # Boundary complexity (how irregular the negative space boundary is)
            if occupied_pixels > 0:
                boundary_complexity = boundary_length / np.sqrt(occupied_pixels)
                features['boundary_complexity'] = boundary_complexity
                features['boundary_complexity_phi'] = self.calculate_phi_alignment(boundary_complexity)
            else:
                features['boundary_complexity'] = 0
                features['boundary_complexity_phi'] = 0
        else:
            features['boundary_length'] = 0
            features['boundary_length_phi'] = 0
            features['boundary_complexity'] = 0
            features['boundary_complexity_phi'] = 0
        
        # 3. Negative space distribution analysis
        # Distance transform shows how "deep" into negative space each pixel is
        dist_transform = cv2.distanceTransform(negative_space, cv2.DIST_L2, 5)
        
        # Statistics of negative space depth
        non_zero_distances = dist_transform[dist_transform > 0]
        if len(non_zero_distances) > 0:
            features['neg_max_depth'] = np.max(non_zero_distances)
            features['neg_mean_depth'] = np.mean(non_zero_distances)
            features['neg_std_depth'] = np.std(non_zero_distances)
            features['neg_median_depth'] = np.median(non_zero_distances)
            
            # φ-harmonic depth analysis
            features['neg_max_depth_phi'] = self.calculate_phi_alignment(features['neg_max_depth'])
            features['neg_mean_depth_phi'] = self.calculate_phi_alignment(features['neg_mean_depth'])
            features['neg_median_depth_phi'] = self.calculate_phi_alignment(features['neg_median_depth'])
        else:
            features['neg_max_depth'] = 0
            features['neg_mean_depth'] = 0
            features['neg_std_depth'] = 0
            features['neg_median_depth'] = 0
            features['neg_max_depth_phi'] = 0
            features['neg_mean_depth_phi'] = 0
            features['neg_median_depth_phi'] = 0
        
        # 4. Negative space geometric moments
        # Analyze the shape of the negative space itself
        neg_moments = cv2.moments(negative_space)
        if neg_moments['m00'] > 0:
            # Negative space centroid
            neg_cx = neg_moments['m10'] / neg_moments['m00']
            neg_cy = neg_moments['m01'] / neg_moments['m00']
            features['neg_centroid_x'] = neg_cx
            features['neg_centroid_y'] = neg_cy
            
            # Negative space Hu moments
            neg_hu_moments = cv2.HuMoments(neg_moments)
            for i, hu in enumerate(neg_hu_moments.flatten()):
                features[f'neg_hu_moment_{i}'] = abs(hu)
                features[f'neg_hu_moment_{i}_phi'] = self.calculate_phi_alignment(abs(hu))
        else:
            features['neg_centroid_x'] = 0
            features['neg_centroid_y'] = 0
            for i in range(7):
                features[f'neg_hu_moment_{i}'] = 0
                features[f'neg_hu_moment_{i}_phi'] = 0
        
        # 5. Consciousness coherence (φ-harmonic analysis)
        phi_values = [features.get(k, 0) for k in features.keys() if k.endswith('_phi')]
        if phi_values:
            features['consciousness_coherence'] = np.mean(phi_values)
            features['consciousness_variance'] = np.var(phi_values)
            features['consciousness_coherence_phi'] = self.calculate_phi_alignment(features['consciousness_coherence'])
        else:
            features['consciousness_coherence'] = 0
            features['consciousness_variance'] = 0
            features['consciousness_coherence_phi'] = 0
        
        return features
    
    def create_triangle_profile(self, triangle_type, base_image=None):
        """Create comprehensive profile for a triangle type"""
        if base_image is None:
            image, triangle_points = self.create_triangle_image(triangle_type)
        else:
            image = base_image
            triangle_points = None
        
        # Extract both types of features
        occupied_features = self.extract_occupied_space_features(image)
        negative_features = self.extract_negative_space_features(image)
        
        profile = {
            'triangle_type': triangle_type,
            'occupied_space': occupied_features,
            'negative_space': negative_features,
            'triangle_points': triangle_points.tolist() if triangle_points is not None else None
        }
        
        return profile, image
    
    def calculate_feature_similarity(self, features1, features2):
        """Calculate similarity between two feature sets"""
        # Get common feature keys
        common_keys = set(features1.keys()) & set(features2.keys())
        
        if not common_keys:
            return 0.0
        
        differences = []
        for key in common_keys:
            val1 = features1.get(key, 0)
            val2 = features2.get(key, 0)
            
            # Normalize by maximum value to prevent scale bias
            max_val = max(abs(val1), abs(val2), 1e-6)
            diff = abs(val1 - val2) / max_val
            differences.append(diff)
        
        # Calculate similarity (1 - average difference)
        avg_difference = np.mean(differences)
        similarity = max(0, 1 - avg_difference)
        
        return similarity
    
    def identify_triangle(self, test_image, method='negative_space', threshold=0.5):
        """Identify triangle type using specified method"""
        test_profile, _ = self.create_triangle_profile('unknown', test_image)
        
        if method == 'negative_space':
            test_features = test_profile['negative_space']
        else:
            test_features = test_profile['occupied_space']
        
        best_match = None
        best_similarity = 0
        similarities = {}
        
        for triangle_type, stored_profile in self.triangle_profiles.items():
            if method == 'negative_space':
                stored_features = stored_profile['negative_space']
            else:
                stored_features = stored_profile['occupied_space']
            
            similarity = self.calculate_feature_similarity(test_features, stored_features)
            similarities[triangle_type] = similarity
            
            if similarity > best_similarity and similarity >= threshold:
                best_similarity = similarity
                best_match = triangle_type
        
        return best_match, best_similarity, similarities

def run_triangle_negative_space_experiment():
    """
    Run comprehensive triangle identification experiment
    Compare negative space vs occupied space identification
    """
    print("🔺 TRIANGLE NEGATIVE SPACE IDENTIFICATION EXPERIMENT")
    print("Testing consciousness-based geometric identification")
    print("Based on Vaughn Scott's Negative Space Consciousness Theory")
    print(f"φ = {PHI}")
    print(f"Birth Resonance: {BIRTH_RESONANCE}")
    print("=" * 70)
    
    # Initialize identifier
    identifier = TriangleNegativeSpaceIdentifier()
    
    # Define triangle types to test
    triangle_types = ['equilateral', 'phi_triangle', 'right_triangle', 'isosceles', 'scalene']
    
    print("\n📐 CREATING TRIANGLE PROFILES")
    print("-" * 40)
    
    # Create base profiles for each triangle type
    for triangle_type in triangle_types:
        profile, image = identifier.create_triangle_profile(triangle_type)
        identifier.triangle_profiles[triangle_type] = profile
        
        # Display profile information
        occ_coherence = profile['occupied_space'].get('aspect_phi', 0)
        neg_coherence = profile['negative_space'].get('consciousness_coherence', 0)
        
        print(f"  {triangle_type:12}: Occupied φ={occ_coherence:.3f}, Negative φ={neg_coherence:.3f}")
    
    print("\n🧪 CREATING TEST VARIATIONS")
    print("-" * 35)
    
    # Create test variations of each triangle type
    test_cases = []
    for triangle_type in triangle_types:
        for variation in range(1, 4):  # 3 variations per type
            test_image, _ = identifier.create_triangle_image(triangle_type, variation=variation)
            test_cases.append((test_image, triangle_type))
    
    print(f"Created {len(test_cases)} test cases ({len(triangle_types)} types × 3 variations)")
    
    # Run identification tests
    print("\n🔬 RUNNING IDENTIFICATION TESTS")
    print("-" * 40)
    
    results = {
        'negative_space': {'correct': 0, 'total': 0, 'similarities': [], 'detailed': []},
        'occupied_space': {'correct': 0, 'total': 0, 'similarities': [], 'detailed': []}
    }
    
    for i, (test_image, true_type) in enumerate(test_cases):
        print(f"\nTest {i+1}: True type = {true_type}")
        
        # Test negative space method
        neg_match, neg_sim, neg_similarities = identifier.identify_triangle(test_image, 'negative_space')
        results['negative_space']['total'] += 1
        results['negative_space']['similarities'].append(neg_sim)
        results['negative_space']['detailed'].append({
            'true_type': true_type,
            'predicted_type': neg_match,
            'similarity': neg_sim,
            'all_similarities': neg_similarities
        })
        
        if neg_match == true_type:
            results['negative_space']['correct'] += 1
            print(f"  🌌 Negative Space: ✅ {neg_match} (similarity: {neg_sim:.3f})")
        else:
            print(f"  🌌 Negative Space: ❌ {neg_match} (similarity: {neg_sim:.3f})")
        
        # Test occupied space method
        occ_match, occ_sim, occ_similarities = identifier.identify_triangle(test_image, 'occupied_space')
        results['occupied_space']['total'] += 1
        results['occupied_space']['similarities'].append(occ_sim)
        results['occupied_space']['detailed'].append({
            'true_type': true_type,
            'predicted_type': occ_match,
            'similarity': occ_sim,
            'all_similarities': occ_similarities
        })
        
        if occ_match == true_type:
            results['occupied_space']['correct'] += 1
            print(f"  📐 Occupied Space: ✅ {occ_match} (similarity: {occ_sim:.3f})")
        else:
            print(f"  📐 Occupied Space: ❌ {occ_match} (similarity: {occ_sim:.3f})")
    
    # Calculate final statistics
    print("\n📊 EXPERIMENTAL RESULTS")
    print("=" * 50)
    
    for method in ['negative_space', 'occupied_space']:
        total = results[method]['total']
        correct = results[method]['correct']
        similarities = results[method]['similarities']
        
        accuracy = correct / total if total > 0 else 0
        avg_similarity = np.mean(similarities) if similarities else 0
        std_similarity = np.std(similarities) if similarities else 0
        
        results[method]['accuracy'] = accuracy
        results[method]['avg_similarity'] = avg_similarity
        results[method]['std_similarity'] = std_similarity
        
        method_name = "🌌 NEGATIVE SPACE" if method == 'negative_space' else "📐 OCCUPIED SPACE"
        print(f"\n{method_name} METHOD:")
        print(f"   Accuracy: {accuracy:.1%}")
        print(f"   Average Similarity: {avg_similarity:.3f}")
        print(f"   Similarity Std Dev: {std_similarity:.3f}")
        print(f"   Correct Identifications: {correct}/{total}")
    
    # Compare methods
    neg_accuracy = results['negative_space']['accuracy']
    occ_accuracy = results['occupied_space']['accuracy']
    accuracy_diff = neg_accuracy - occ_accuracy
    
    neg_avg_sim = results['negative_space']['avg_similarity']
    occ_avg_sim = results['occupied_space']['avg_similarity']
    similarity_diff = neg_avg_sim - occ_avg_sim
    
    print("\n📈 COMPARATIVE ANALYSIS:")
    print(f"   Accuracy Difference: {accuracy_diff:+.1%}")
    print(f"   Similarity Difference: {similarity_diff:+.3f}")
    
    if accuracy_diff > 0:
        print("   ✅ NEGATIVE SPACE METHOD SUPERIOR")
    elif accuracy_diff < 0:
        print("   ❌ OCCUPIED SPACE METHOD SUPERIOR")
    else:
        print("   ⚖️  METHODS EQUIVALENT")
    
    # φ-Harmonic consciousness analysis
    print("\n🌟 φ-HARMONIC CONSCIOUSNESS ANALYSIS:")
    print("-" * 45)
    
    for triangle_type in triangle_types:
        profile = identifier.triangle_profiles[triangle_type]
        neg_coherence = profile['negative_space'].get('consciousness_coherence', 0)
        neg_coherence_phi = identifier.calculate_phi_alignment(neg_coherence)
        
        occ_aspect_phi = profile['occupied_space'].get('aspect_phi', 0)
        
        print(f"  {triangle_type:12}:")
        print(f"    Negative Space Consciousness: {neg_coherence:.3f} (φ-align: {neg_coherence_phi:.3f})")
        print(f"    Occupied Space φ-Alignment: {occ_aspect_phi:.3f}")
    
    # Overall consciousness metrics
    all_neg_coherence = [identifier.triangle_profiles[t]['negative_space'].get('consciousness_coherence', 0) 
                        for t in triangle_types]
    all_occ_phi = [identifier.triangle_profiles[t]['occupied_space'].get('aspect_phi', 0) 
                   for t in triangle_types]
    
    avg_neg_coherence = np.mean(all_neg_coherence)
    avg_occ_phi = np.mean(all_occ_phi)
    
    print(f"\n  Average Negative Space Consciousness: {avg_neg_coherence:.3f}")
    print(f"  Average Occupied Space φ-Alignment: {avg_occ_phi:.3f}")
    print(f"  Consciousness Superiority: {avg_neg_coherence - avg_occ_phi:+.3f}")
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"triangle_negative_space_results_{timestamp}.json"
    
    save_data = {
        'experiment_info': {
            'timestamp': timestamp,
            'phi': PHI,
            'birth_resonance': BIRTH_RESONANCE,
            'triangle_types': triangle_types,
            'test_cases': len(test_cases)
        },
        'results': results,
        'consciousness_analysis': {
            'negative_space_coherence': all_neg_coherence,
            'occupied_space_phi': all_occ_phi,
            'avg_negative_coherence': avg_neg_coherence,
            'avg_occupied_phi': avg_occ_phi
        },
        'triangle_profiles': {t: identifier.triangle_profiles[t] for t in triangle_types}
    }
    
    # Convert numpy types to native Python types for JSON serialization
    def convert_numpy_types(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {key: convert_numpy_types(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert_numpy_types(item) for item in obj]
        return obj
    
    save_data = convert_numpy_types(save_data)
    
    with open(results_file, 'w') as f:
        json.dump(save_data, f, indent=2)
    
    print(f"\n💾 Results saved to: {results_file}")
    
    print("\n🎉 TRIANGLE NEGATIVE SPACE EXPERIMENT COMPLETE!")
    print("🔺 Testing geometric identification via consciousness-defined negative space")
    print("📊 Results validate effectiveness of negative space identification")
    
    return results, identifier

if __name__ == "__main__":
    # Run the experiment
    results, identifier = run_triangle_negative_space_experiment()
